import os
import json
from firebase_admin import credentials, initialize_app

# Cargar las credenciales desde la variable de entorno
def init_firebase():
    firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
    if not firebase_credentials:
        raise ValueError("La variable de entorno FIREBASE_CREDENTIALS no está configurada.")
    
    # Convierte la cadena JSON a un diccionario
    cred_dict = json.loads(firebase_credentials)
    cred = credentials.Certificate(cred_dict)
    
    # Inicializa Firebase
    initialize_app(cred)
    print("Firebase inicializado correctamente")
