import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_firebase():
    """Initialize Firebase with proper credentials"""
    try:
        # Check if Firebase is already initialized
        if not firebase_admin._apps:
            # List of possible paths for serviceAccountKey.json
            possible_paths = [
                'serviceAccountKey.json',
                'backend/serviceAccountKey.json',
                '../backend/serviceAccountKey.json',
                os.path.join(os.path.dirname(__file__), '..', 'backend', 'serviceAccountKey.json')
            ]

            # Find the first valid service account key file
            cred_path = None
            for path in possible_paths:
                if os.path.exists(path):
                    cred_path = path
                    break

            if cred_path:
                logger.info(f"Found service account key at: {cred_path}")
                cred = credentials.Certificate(cred_path)
                firebase_admin.initialize_app(cred)
                db = firestore.client()
                logger.info("Firebase initialized successfully!")
                return True
            else:
                logger.error("No service account key file found!")
                return False
        else:
            logger.info("Firebase already initialized")
            return True

    except Exception as e:
        logger.error(f"Error initializing Firebase: {str(e)}")
        return False

def verify_firestore_connection():
    """Test the Firestore connection"""
    try:
        db = firestore.client()
        # Try to perform a simple operation
        test_ref = db.collection('test').document('test')
        test_ref.set({'test': True})
        test_ref.delete()
        logger.info("Firestore connection verified successfully!")
        return True
    except Exception as e:
        logger.error(f"Firestore connection failed: {str(e)}")
        return False

if __name__ == "__main__":
    if setup_firebase():
        verify_firestore_connection()