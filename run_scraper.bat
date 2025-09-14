@echo off
echo Setting up Python environment for scraping...

REM Set SSL certificate path
set SSL_CERT_FILE=C:/Users/Jyothika/Desktop/jannat_audit/.venv/Lib/site-packages/certifi/cacert.pem
set PYTHONHTTPSVERIFY=0

REM Install specific versions of dependencies
call C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/pip.exe install selenium==4.9.1
call C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/pip.exe install webdriver-manager==3.8.6
call C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/pip.exe install certifi==2024.2.2

REM Run the scraper
call C:/Users/Jyothika/Desktop/jannat_audit/.venv/Scripts/python.exe python_scripts/government_portal_scraper.py

pause