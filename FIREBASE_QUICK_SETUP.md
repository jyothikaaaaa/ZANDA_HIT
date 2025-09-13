# Quick Firebase Setup for "junta" Project

## 🚀 **Your Firebase Project Details**
- **Project Name**: junta
- **Project ID**: junta-d7181
- **URL**: https://console.firebase.google.com/u/0/project/junta-d7181

## ⚡ **Quick Setup Steps**

### 1. Enable Firestore Database
1. Go to your Firebase Console: https://console.firebase.google.com/u/0/project/junta-d7181
2. Click **"Firestore Database"** in the left sidebar
3. Click **"Create database"**
4. Choose **"Start in test mode"** (for development)
5. Select a location (choose closest to India)

### 2. Get Your Web App Configuration
1. Click the **gear icon** (⚙️) next to "Project Overview"
2. Scroll down to **"Your apps"** section
3. If you don't have a web app:
   - Click **"Add app"**
   - Select the **Web icon** (`</>`)
   - App nickname: `Janata Audit Web`
   - Click **"Register app"**
4. Copy the configuration object

### 3. Update firebase-config.js
Replace the placeholder values in `firebase-config.js` with your actual configuration.

## 🔧 **Current Configuration**
I've already updated your `firebase-config.js` with:
- ✅ **Project ID**: junta-d7181
- ✅ **Auth Domain**: junta-d7181.firebaseapp.com
- ✅ **Storage Bucket**: junta-d7181.appspot.com
- ⚠️ **API Key**: Using Google Maps key (needs Firebase key)
- ⚠️ **Messaging Sender ID**: Placeholder (needs actual value)
- ⚠️ **App ID**: Placeholder (needs actual value)

## 🧪 **Test the Setup**
1. Open `index.html` in your browser
2. Try to sign in with any details
3. Check browser console for Firebase messages
4. Check Firestore Database for new user documents

## 📊 **What You Should See**
- **Browser Console**: "Firebase initialized successfully"
- **Firestore Database**: New documents in `users` collection
- **Authentication**: Users appearing in the Users tab

## 🚨 **If You See Errors**
- **"Firebase config not found"**: Update firebase-config.js with actual values
- **"Permission denied"**: Check Firestore security rules
- **"API key invalid"**: Get the correct Firebase API key (not Google Maps key)

---

**Your Firebase project is ready! Just need to complete the web app configuration.** 🎉
