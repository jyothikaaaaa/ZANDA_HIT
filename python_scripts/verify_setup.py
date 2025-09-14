import logging
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib3
import certifi
import ssl

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def verify_ssl_setup():
    """Verify SSL certificate setup"""
    try:
        # Create SSL context with proper certificates
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        logger.info("SSL context created successfully")
        
        # Disable SSL warnings for our scraping
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Test HTTPS request with proper SSL verification
        test_url = "https://www.google.com"
        response = requests.get(test_url, verify=certifi.where())
        response.raise_for_status()
        logger.info("SSL verification working correctly")
        return True
    except Exception as e:
        logger.error(f"SSL setup error: {str(e)}")
        return False

def verify_chrome_setup():
    """Verify Chrome WebDriver setup"""
    try:
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--ignore-certificate-errors')
        
        # Setup Chrome driver
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        # Test the driver
        driver.get("https://www.google.com")
        logger.info("Chrome WebDriver working correctly")
        
        driver.quit()
        return True
    except Exception as e:
        logger.error(f"Chrome setup error: {str(e)}")
        return False

if __name__ == "__main__":
    logger.info("Verifying system setup...")
    ssl_ok = verify_ssl_setup()
    chrome_ok = verify_chrome_setup()
    
    if ssl_ok and chrome_ok:
        logger.info("All systems verified and working correctly!")
    else:
        logger.error("Some verifications failed. Please check the logs above.")