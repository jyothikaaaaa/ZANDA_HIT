# 🏛️ Janata Audit Bengaluru

An AI-Powered Civic Accountability Platform for tracking local government infrastructure projects, public funds, and political donations in Bengaluru.

## 🎯 Project Overview

Janata Audit: Bengaluru is a comprehensive web platform that empowers citizens to monitor and track civic projects, detect anomalies using AI, and provide crowdsourced feedback. The platform focuses specifically on Bengaluru's civic bodies and provides transparency in government spending and project execution.

## ✨ Features

### ✅ **Current Features (HTML Version)**
- **Interactive Map**: Google Maps integration with project markers
- **Project Tracking**: Monitor infrastructure projects across Bengaluru  
- **Filtering System**: Filter by ward, department, and status
- **Responsive Design**: Works on desktop and mobile
- **Project Details**: Detailed project information modal
- **User Authentication**: Phone-based login with Firebase integration
- **Modern UI**: Clean, professional design with animations

### 🔮 **Planned Features**
- **AI Anomaly Detection**: Automated detection of suspicious patterns
- **Satellite Analysis**: Google Earth Engine integration for physical verification
- **Delay Prediction**: ML-powered project delay risk assessment
- **Real-time Updates**: Live data synchronization
- **Crowdsourced Feedback**: Citizen input and photo submissions

## 🏗️ Architecture

- **Frontend**: HTML/CSS/JavaScript (simplified from React.js)
- **Backend**: Express.js server with Firebase Admin SDK
- **Database**: Firestore (Firebase)
- **Authentication**: Phone number OTP verification
- **Maps**: Google Maps JavaScript API
- **Deployment**: Static hosting (Netlify/Vercel) + Render (backend)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/jyothikaaaaa/junta.git
cd junta
```

### 2. Set Up Firebase Configuration
```bash
# Copy the template file
cp firebase-config.template.js firebase-config.js

# Edit firebase-config.js with your Firebase project details
```

### 3. Get Required API Keys
- **Firebase Configuration**: From Firebase Console
- **Google Maps API Key**: From Google Cloud Console

### 4. Run the Application
```bash
# Simply open in browser
start index.html

# Or serve locally
python -m http.server 8000
# Visit http://localhost:8000
```

## 📋 Setup Requirements

### Firebase Setup
1. Create a Firebase project at https://console.firebase.google.com/
2. Enable Firestore Database
3. Enable Authentication (Phone provider)
4. Get your web app configuration
5. Update `firebase-config.js` with your credentials

### Google Maps Setup
1. Get API key from Google Cloud Console
2. Enable Maps JavaScript API
3. Replace `YOUR_API_KEY_HERE` in `index.html`

## 📁 Project Structure

```
├── index.html              # Main HTML application
├── styles.css              # CSS styling
├── script.js               # JavaScript functionality
├── firebase-config.template.js  # Firebase config template
├── test-firebase.html      # Firebase connection test page
├── backend/                # Express.js backend
│   ├── server.js
│   └── package.json
├── python_scripts/         # Data scraping and AI analysis
├── functions/              # Firebase Cloud Functions
└── docs/                   # Documentation
    ├── GOOGLE_MAPS_SETUP.md
    ├── FIREBASE_SETUP.md
    └── HTML_README.md
```

## 🔧 Configuration

### Environment Variables
Create `.env` file in root directory:
```env
# Firebase Configuration (for backend)
FIREBASE_SERVICE_ACCOUNT_KEY={"type":"service_account",...}
FIREBASE_DATABASE_URL=https://your-project.firebaseio.com

# Google Maps API Key
REACT_APP_GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

### Firebase Configuration
Update `firebase-config.js`:
```javascript
const firebaseConfig = {
    apiKey: "your_firebase_api_key",
    authDomain: "your_project.firebaseapp.com",
    projectId: "your_project_id",
    storageBucket: "your_project.appspot.com",
    messagingSenderId: "your_sender_id",
    appId: "your_app_id"
};
```

## 🎯 Government Data Sources

- Bruhat Bengaluru Mahanagara Palike (BBMP)
- Bangalore Development Authority (BDA)  
- Bangalore Metro Rail Corporation Ltd (BMRCL)
- Bangalore Water Supply and Sewerage Board (BWSSB)
- Bangalore Electricity Supply Company (BESCOM)
- Karnataka Public Works Department (PWD)
- Election Commission of India (Political Donations)

## 🤖 AI Features (Planned)

### Anomaly Detection
- Budget anomalies detection
- Timeline irregularities
- Contractor allocation patterns
- Political donation correlations

### Satellite Inspector
- Google Earth Engine integration
- NDBI (Normalized Difference Built-up Index) analysis
- Before/after project comparison
- Physical verification against claims

## 📱 Usage

### For Citizens
1. **Sign Up**: Register with phone number and ward information
2. **Browse Projects**: View projects on interactive map
3. **Filter & Search**: Find projects by ward, department, or budget
4. **Provide Feedback**: Submit ratings, comments, and photos
5. **Report Issues**: Flag suspicious activities or anomalies

### For Administrators  
1. **Monitor AI Flags**: Review automated anomaly detection
2. **Manage Projects**: Approve crowdsourced project submissions
3. **Analyze Data**: View comprehensive project analytics
4. **Update Status**: Modify project information and status

## 🚀 Deployment

### Frontend (Static Hosting)
```bash
# Deploy to Netlify
npm run build
# Connect GitHub repository to Netlify

# Deploy to Vercel
# Connect GitHub repository to Vercel
```

### Backend (Render)
```bash
# Follow RENDER_DEPLOYMENT.md for detailed instructions
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Documentation**: Check the `docs/` folder for detailed guides
- **Issues**: Create an issue in this repository
- **Discussions**: Use GitHub Discussions for questions and ideas

## 🔮 Roadmap

- [ ] Complete Firebase integration
- [ ] Add real-time data synchronization
- [ ] Implement AI anomaly detection
- [ ] Add satellite imagery analysis
- [ ] Mobile app development
- [ ] Advanced analytics dashboard
- [ ] Multi-language support

---

**Janata Audit: Bengaluru** - Empowering citizens through transparency and accountability.

Built with ❤️ for the people of Bengaluru.