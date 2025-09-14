#!/usr/bin/env python3
"""
Simple HTTP server using http.server with better port handling
"""

import http.server
import socketserver
import json
import os
import subprocess
import sys
import webbrowser
import time
from urllib.parse import urlparse, parse_qs

class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        if self.path == '/api/projects':
            self.handle_projects_api()
        elif self.path == '/api/health':
            self.handle_health_api()
        elif self.path == '/':
            self.path = '/index.html'
            super().do_GET()
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == '/api/scrape':
            self.handle_scrape_api()
        else:
            self.send_error(404, "Not Found")
    
    def handle_projects_api(self):
        try:
            if os.path.exists('bengaluru_projects.json'):
                with open('bengaluru_projects.json', 'r', encoding='utf-8') as f:
                    projects = json.load(f)
            else:
                projects = get_mock_projects()
            
            response_data = {
                'success': True,
                'projects': projects,
                'total': len(projects)
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
            
        except Exception as e:
            self.send_error(500, f"Error: {str(e)}")
    
    def handle_health_api(self):
        response_data = {'status': 'OK', 'message': 'Server running'}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())
    
    def handle_scrape_api(self):
        try:
            result = subprocess.run([
                sys.executable, 'python_scripts/bengaluru_project_scraper.py'
            ], capture_output=True, text=True, timeout=600)
            
            if result.returncode == 0 and os.path.exists('bengaluru_projects.json'):
                with open('bengaluru_projects.json', 'r', encoding='utf-8') as f:
                    projects = json.load(f)
                
                response_data = {
                    'success': True,
                    'count': len(projects),
                    'message': f'Successfully scraped {len(projects)} projects'
                }
            else:
                response_data = {
                    'success': False,
                    'error': 'Scraper failed or no projects found'
                }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())
            
        except Exception as e:
            response_data = {'success': False, 'error': str(e)}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode())

def get_mock_projects():
    return [
        {
            'id': '1',
            'projectName': 'BBMP Road Infrastructure Development',
            'description': 'Comprehensive road development project in Ward 15',
            'status': 'In Progress',
            'budget': 50000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'BBMP',
            'wardNumber': 15,
            'geoPoint': {'latitude': 12.9716, 'longitude': 77.5946},
            'contractor': 'ABC Construction Ltd.',
            'startDate': '2023-01-15',
            'endDate': '2024-12-31',
            'source': 'BBMP',
            'sourceUrl': 'https://bbmp.gov.in/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        },
        {
            'id': '2',
            'projectName': 'BDA Housing Scheme Phase 2',
            'description': 'Affordable housing project for middle-income families',
            'status': 'Completed',
            'budget': 75000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'BDA',
            'wardNumber': 8,
            'geoPoint': {'latitude': 12.9352, 'longitude': 77.6245},
            'contractor': 'XYZ Builders',
            'startDate': '2022-06-01',
            'endDate': '2023-11-30',
            'source': 'BDA',
            'sourceUrl': 'https://bdabangalore.org/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        },
        {
            'id': '3',
            'projectName': 'BWSSB Water Supply Network',
            'description': 'New water supply network for expanding areas',
            'status': 'Pending',
            'budget': 30000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'BWSSB',
            'wardNumber': 22,
            'geoPoint': {'latitude': 12.9141, 'longitude': 77.6781},
            'contractor': 'Water Works Ltd.',
            'startDate': '2024-01-01',
            'endDate': '2024-12-31',
            'source': 'BWSSB',
            'sourceUrl': 'https://bwssb.karnataka.gov.in/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        },
        {
            'id': '4',
            'projectName': 'BMRCL Metro Line Extension',
            'description': 'Extension of metro line to new areas',
            'status': 'In Progress',
            'budget': 120000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'BMRCL',
            'wardNumber': 12,
            'geoPoint': {'latitude': 12.9858, 'longitude': 77.6101},
            'contractor': 'Metro Construction Co.',
            'startDate': '2023-03-01',
            'endDate': '2025-06-30',
            'source': 'BMRCL',
            'sourceUrl': 'https://english.bmrc.co.in/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        },
        {
            'id': '5',
            'projectName': 'BESCOM Electrical Infrastructure',
            'description': 'Upgradation of electrical infrastructure',
            'status': 'In Progress',
            'budget': 40000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'BESCOM',
            'wardNumber': 18,
            'geoPoint': {'latitude': 12.9230, 'longitude': 77.5933},
            'contractor': 'Power Solutions Inc.',
            'startDate': '2023-08-01',
            'endDate': '2024-08-31',
            'source': 'BESCOM',
            'sourceUrl': 'https://bescom.karnataka.gov.in/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        },
        {
            'id': '6',
            'projectName': 'KPWD Bridge Construction',
            'description': 'New bridge construction over river',
            'status': 'Pending',
            'budget': 60000000,
            'location': 'Bengaluru, Karnataka',
            'department': 'KPWD',
            'wardNumber': 25,
            'geoPoint': {'latitude': 12.9569, 'longitude': 77.7011},
            'contractor': 'Bridge Builders Ltd.',
            'startDate': '2024-02-01',
            'endDate': '2025-01-31',
            'source': 'KPWD',
            'sourceUrl': 'https://kpwd.karnataka.gov.in/',
            'scrapedAt': '2023-12-01T10:30:00Z'
        }
    ]

def find_free_port():
    """Find a free port starting from 8000"""
    import socket
    for port in range(8000, 8100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    return None

def main():
    print("🚀 Starting Janata Audit Bengaluru")
    print("=" * 50)
    
    # Find a free port
    port = find_free_port()
    if port is None:
        print("❌ Could not find a free port. Please close some applications and try again.")
        return
    
    print(f"✅ Found free port: {port}")
    print(f"🌐 Starting server on http://localhost:{port}")
    
    try:
        with socketserver.TCPServer(("", port), SimpleHandler) as httpd:
            print(f"✅ Server started successfully!")
            print(f"🌐 Open http://localhost:{port} in your browser")
            print(f"📝 Press Ctrl+C to stop")
            print("=" * 50)
            
            # Open browser after a short delay
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{port}')
            
            import threading
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Server error: {e}")
        print("💡 Try running as administrator or check firewall settings")

if __name__ == "__main__":
    main()
