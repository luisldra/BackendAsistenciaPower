import os
import json
from firebase_admin import credentials, initialize_app

def init_firebase():
    # Leer las credenciales desde la variable de entorno
    firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
    if not firebase_credentials:
        raise ValueError("La variable de entorno FIREBASE_CREDENTIALS no está configurada.")
    
    # Convertir el JSON en un diccionario
    cred_dict = json.loads(firebase_credentials)
    cred = credentials.Certificate(cred_dict)
    
    # Inicializar Firebase
    initialize_app(cred)
    print("Firebase inicializado correctamente")
