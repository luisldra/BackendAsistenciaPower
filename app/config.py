import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Conexión con Firestore
db = firestore.client()

