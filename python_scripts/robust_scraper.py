import logging
import json
import requests
import firebase_admin
from firebase_admin import credentials, firestore
from bs4 import BeautifulSoup
from datetime import datetime
import os
from urllib.parse import urljoin
import urllib3

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class RobustScraper:
    def __init__(self):
        self.projects = []
        self.setup_firebase()
        self.session = requests.Session()
        # Use a recent browser User-Agent
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })

    def setup_firebase(self):
        try:
            if not firebase_admin._apps:
                cred_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'serviceAccountKey.json')
                if os.path.exists(cred_path):
                    cred = credentials.Certificate(cred_path)
                    firebase_admin.initialize_app(cred)
                self.db = firestore.client()
                logger.info("Firebase initialized successfully")
            else:
                self.db = firestore.client()
        except Exception as e:
            logger.error(f"Firebase initialization error: {str(e)}")
            self.db = None

    def safe_request(self, url, timeout=10):
        """Make a request with fallback options"""
        try:
            # Try HTTPS first
            response = self.session.get(url, verify=False, timeout=timeout)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            # Try HTTP if HTTPS fails
            try:
                http_url = url.replace('https://', 'http://')
                response = self.session.get(http_url, verify=False, timeout=timeout)
                response.raise_for_status()
                return response.text
            except requests.exceptions.RequestException as e2:
                logger.error(f"Error fetching {url}: {str(e2)}")
                return None

    def extract_project_info(self, text, source):
        """Extract project information from HTML content"""
        if not text:
            return []

        soup = BeautifulSoup(text, 'html.parser')
        projects = []

        # Look for common project indicators
        selectors = [
            'table tr',  # Table rows
            'div.project',  # Project divs
            'div.tender',  # Tender divs
            'div.work-item',  # Work items
            'article',  # Article elements
            'div.card',  # Card elements
        ]

        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                # Try to extract project information
                name = element.get_text(strip=True)
                if len(name) > 10:  # Filter out too short texts
                    project = {
                        'name': name[:500],  # Limit name length
                        'source': source,
                        'url': source,
                        'scraped_date': datetime.now().isoformat(),
                        'status': 'pending'
                    }
                    projects.append(project)

        return projects

    def scrape_portals(self):
        """Scrape all government portals"""
        portals = {
            'BBMP': 'http://bbmp.gov.in/en/web/guest/projects',
            'BDA': 'http://www.bdabangalore.org/projects.html',
            'BWSSB': 'http://www.bwssb.gov.in/projects',
            'BMRCL': 'http://www.bmrc.co.in/projects.html',
            'BESCOM': 'http://bescom.org/projects/',
            'KPWD': 'http://www.kpwd.gov.in/projects.html',
            'KUIDFC': 'http://www.kuidfc.com/projects.html',
            'BMTC': 'http://www.mybmtc.com/projects'
        }

        for portal_name, url in portals.items():
            logger.info(f"Scraping {portal_name}...")
            content = self.safe_request(url)
            if content:
                portal_projects = self.extract_project_info(content, portal_name)
                self.projects.extend(portal_projects)
                logger.info(f"Found {len(portal_projects)} projects from {portal_name}")

    def save_results(self):
        """Save results to file and Firestore"""
        # Save to file
        try:
            with open('scraped_projects.json', 'w', encoding='utf-8') as f:
                json.dump(self.projects, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved {len(self.projects)} projects to file")
        except Exception as e:
            logger.error(f"Error saving to file: {str(e)}")

        # Save to Firestore
        if self.db:
            try:
                batch = self.db.batch()
                collection = self.db.collection('scraped_projects')
                
                for project in self.projects:
                    doc_ref = collection.document()
                    batch.set(doc_ref, project)
                
                batch.commit()
                logger.info(f"Saved {len(self.projects)} projects to Firestore")
            except Exception as e:
                logger.error(f"Error saving to Firestore: {str(e)}")

def main():
    scraper = RobustScraper()
    scraper.scrape_portals()
    scraper.save_results()

    # Print summary
    print("\n=== Scraping Summary ===")
    print(f"Total projects found: {len(scraper.projects)}")
    print("\nProjects by source:")
    sources = {}
    for project in scraper.projects:
        sources[project['source']] = sources.get(project['source'], 0) + 1
    for source, count in sources.items():
        print(f"{source}: {count} projects")

if __name__ == "__main__":
    main()