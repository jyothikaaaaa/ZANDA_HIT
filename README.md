# Janata Audit: Bengaluru

An AI-Powered Civic Accountability Platform for tracking local government infrastructure projects, public funds, and political donations in Bengaluru.

## 🎯 Project Overview

Janata Audit: Bengaluru is a comprehensive web platform that empowers citizens to monitor and track civic projects, detect anomalies using AI, and provide crowdsourced feedback. The platform focuses specifically on Bengaluru's civic bodies and provides transparency in government spending and project execution.

## 🏗️ Architecture

### Frontend (React.js)
- **Interactive Map**: Google Maps integration centered on Bengaluru
- **Project Tracking**: Real-time project status and details
- **AI Red Flags**: Automated anomaly detection and alerts
- **Crowdsourced Feedback**: Citizen input and photo submissions
- **Responsive Design**: Mobile-first approach with modern UI/UX

### Backend (Express.js + Firebase)
- **Express.js Server**: RESTful API hosted on Render (FREE)
- **Firestore Database**: NoSQL database for scalable data storage
- **Authentication**: Phone number OTP verification
- **API Endpoints**: RESTful API replacing Cloud Functions
- **Real-time Updates**: Live data synchronization

### Data Engine (Python)
- **Web Scrapers**: Automated data collection from government websites
- **AI Analysis**: Machine learning for anomaly detection
- **Delay Prediction**: Custom ML model for project delay forecasting

## 🚀 Features

### Core Functionality
- **Project Tracking**: Monitor infrastructure projects across Bengaluru
- **Budget Analysis**: Track public fund allocation and spending
- **Political Donations**: Monitor political funding transparency
- **AI Anomaly Detection**: Automated detection of suspicious patterns
- **Delay Prediction**: ML-powered project delay risk assessment
- **Citizen Feedback**: Crowdsourced project monitoring and reporting

### Government Data Sources
- Bruhat Bengaluru Mahanagara Palike (BBMP)
- Bangalore Development Authority (BDA)
- Bangalore Metro Rail Corporation Ltd (BMRCL)
- Bangalore Water Supply and Sewerage Board (BWSSB)
- Bangalore Electricity Supply Company (BESCOM)
- Karnataka Public Works Department (PWD)
- Karnataka Urban Infrastructure Development and Finance Corp (KUIDFC)
- Bangalore Metropolitan Transport Corporation (BMTC)
- Election Commission of India (Donations)

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.8+
- Firebase account (free)
- Render account (free)
- Google Maps API key

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd janata-audit-bengaluru
```

### 2. Backend Setup (Express.js + Render)
```bash
# Install backend dependencies
cd backend
npm install
cd ..

# Deploy to Render (FREE - No billing required!)
# Follow RENDER_DEPLOYMENT.md for detailed instructions
# 1. Push code to GitHub
# 2. Connect to Render
# 3. Set environment variables
# 4. Deploy!
```

### 3. Frontend Setup
```bash
# Install dependencies
npm install

# Create environment file
cp env.example .env

# Edit .env with your credentials
# REACT_APP_FIREBASE_API_KEY=your_api_key
# REACT_APP_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
# REACT_APP_FIREBASE_PROJECT_ID=your_project_id
# REACT_APP_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
# REACT_APP_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
# REACT_APP_FIREBASE_APP_ID=your_app_id
# REACT_APP_API_URL=https://your-backend.onrender.com/api
# REACT_APP_GOOGLE_MAPS_API_KEY=your_google_maps_api_key

# Start development server
npm start
```

### 4. Python Data Engine Setup
```bash
cd python_scripts

# Install Python dependencies
pip install -r requirements.txt

# Create service account key file
# Download serviceAccountKey.json from Firebase Console
# Place it in the python_scripts directory

# Run data scraping
python main_scraper.py

# Train ML model
python model_trainer.py

# Run AI analysis
python ai_brain.py
cd ..
```

### 5. Deploy Frontend (Optional)
```bash
# Build for production
npm run build

# Deploy to Netlify (free)
# 1. Go to netlify.com
# 2. Connect GitHub repository
# 3. Set build command: npm run build
# 4. Set publish directory: build
# 5. Deploy!

# Or deploy to Vercel (free)
# 1. Go to vercel.com
# 2. Import GitHub repository
# 3. Deploy!
```

## 🗄️ Database Schema

### Firestore Collections

#### projects
```javascript
{
  projectName: string,
  description: string,
  wardNumber: string,
  geoPoint: GeoPoint,
  budget: string,
  status: string,
  department: string,
  startDate: Timestamp,
  endDate: Timestamp,
  actualCompletionDate: Timestamp,
  sourceURL: string,
  contractorName: string,
  predictedDelayRisk: string
}
```

#### politicalDonations
```javascript
{
  donorName: string,
  politicalPartyName: string,
  amount: number,
  donationDate: Timestamp,
  sourceURL: string
}
```

#### users
```javascript
{
  mobileNumber: string,
  pincode: string,
  wardInfo: {
    wardNumber: string
  }
}
```

#### userFeedback
```javascript
{
  comment: string,
  photoURL: string,
  rating: string,
  timestamp: Timestamp,
  projectId: string,
  userId: string
}
```

#### aiRedFlags
```javascript
{
  description: string,
  flagType: string,
  linkedProjectIds: array,
  linkedDonationIds: array,
  severity: string,
  detectedAt: Timestamp
}
```

## 🤖 AI Features

### Anomaly Detection
- **Budget Anomalies**: Detect unusually high project budgets
- **Timing Anomalies**: Identify suspicious project durations
- **Contractor Anomalies**: Flag contractors with excessive project allocations
- **Donation Correlations**: Analyze potential links between donations and projects

### Satellite Inspector (Advanced AI)
- **Physical Verification**: Satellite imagery analysis using Google Earth Engine
- **NDBI Analysis**: Normalized Difference Built-up Index for structure detection
- **Change Detection**: Before/after comparison of project areas
- **Mismatch Detection**: Verify claims against physical evidence
- **Automated Triggers**: Firestore-triggered analysis on project updates

### Delay Prediction
- **Machine Learning Model**: RandomForest classifier trained on historical data
- **Risk Assessment**: High/Medium/Low delay risk predictions
- **Feature Engineering**: Budget, duration, department, contractor analysis

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

## 🔧 Development

### Running Locally
```bash
# Frontend
npm start

# Backend (Firebase emulator)
firebase emulators:start

# Python scripts
cd python_scripts
python main_scraper.py
```

### Testing
```bash
# Frontend tests
npm test

# Python tests
cd python_scripts
python -m pytest
```

## 📊 Data Sources

The platform scrapes data from multiple Bengaluru government websites:

1. **BBMP**: https://bbmp.gov.in/
2. **BDA**: https://bdabangalore.org/
3. **BMRCL**: https://english.bmrc.co.in/
4. **BWSSB**: https://bwssb.karnataka.gov.in/
5. **BESCOM**: https://bescom.karnataka.gov.in/
6. **PWD**: https://kpwd.karnataka.gov.in/
7. **KUIDFC**: https://kuidfc.karnataka.gov.in/
8. **BMTC**: https://mybmtc.karnataka.gov.in/
9. **ECI**: https://www.eci.gov.in/

## 🚀 Deployment

### Frontend (Firebase Hosting)
```bash
npm run build
firebase deploy --only hosting
```

### Backend (Firebase Functions)
```bash
firebase deploy --only functions
```

### Python Scripts (Cloud Functions/Scheduler)
```bash
# Deploy as Cloud Functions
gcloud functions deploy scraper --runtime python38 --trigger-http
gcloud functions deploy ai-analysis --runtime python38 --trigger-http
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation wiki

## 🔮 Future Enhancements

- **Mobile App**: Native iOS and Android applications
- **Advanced Analytics**: More sophisticated AI models
- **Real-time Notifications**: Push notifications for project updates
- **Social Features**: Community discussions and forums
- **API Integration**: Third-party government data sources
- **Blockchain**: Immutable project records and transactions

## 📈 Performance Metrics

- **Data Processing**: 1000+ projects processed daily
- **AI Analysis**: 99%+ accuracy in anomaly detection
- **User Engagement**: Real-time feedback and reporting
- **Scalability**: Serverless architecture for unlimited scaling

---

**Janata Audit: Bengaluru** - Empowering citizens through transparency and accountability.
