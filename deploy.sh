#!/bin/bash

# Janata Audit Bengaluru - Deployment Script

echo "🚀 Starting deployment of Janata Audit Bengaluru..."

# Check if Firebase CLI is installed
if ! command -v firebase &> /dev/null; then
    echo "❌ Firebase CLI not found. Please install it first:"
    echo "npm install -g firebase-tools"
    exit 1
fi

# Check if user is logged in to Firebase
if ! firebase projects:list &> /dev/null; then
    echo "❌ Please login to Firebase first:"
    echo "firebase login"
    exit 1
fi

# Build React app
echo "📦 Building React application..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Build failed. Please check for errors."
    exit 1
fi

# Deploy Firebase functions
echo "🔧 Deploying Firebase functions..."
cd functions
npm install
cd ..

firebase deploy --only functions

if [ $? -ne 0 ]; then
    echo "❌ Functions deployment failed."
    exit 1
fi

# Deploy Firestore rules
echo "📋 Deploying Firestore rules..."
firebase deploy --only firestore:rules

if [ $? -ne 0 ]; then
    echo "❌ Firestore rules deployment failed."
    exit 1
fi

# Deploy Firestore indexes
echo "📊 Deploying Firestore indexes..."
firebase deploy --only firestore:indexes

if [ $? -ne 0 ]; then
    echo "❌ Firestore indexes deployment failed."
    exit 1
fi

# Deploy hosting
echo "🌐 Deploying to Firebase Hosting..."
firebase deploy --only hosting

if [ $? -ne 0 ]; then
    echo "❌ Hosting deployment failed."
    exit 1
fi

echo "✅ Deployment completed successfully!"
echo "🎉 Janata Audit Bengaluru is now live!"

# Display deployment URLs
echo ""
echo "📱 Application URLs:"
firebase hosting:channel:list

echo ""
echo "🔧 Next steps:"
echo "1. Set up your environment variables in Firebase Functions"
echo "2. Configure your Google Maps API key"
echo "3. Run the Python data scraping scripts"
echo "4. Train the ML model for delay prediction"
echo ""
echo "📚 For more information, check the README.md file"
