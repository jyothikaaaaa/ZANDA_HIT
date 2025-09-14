#!/bin/bash

echo "🚀 Janata Audit Bengaluru - Auto Start"
echo "================================================"
echo "This will automatically:"
echo "1. Run the government data scraper"
echo "2. Start the backend server"
echo "3. Start the frontend server"
echo "4. Open the application in your browser"
echo "================================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed or not in PATH"
    echo "Please install Python from https://python.org"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed or not in PATH"
    echo "Please install Node.js from https://nodejs.org"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Please run this script from the project root directory"
    exit 1
fi

echo "✅ Python and Node.js are installed"
echo

# Make the script executable
chmod +x "$0"

# Run the auto-start script
echo "🚀 Starting the application..."
python3 auto_start.py
