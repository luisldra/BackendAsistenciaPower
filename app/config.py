import os  # Para leer variables de entorno
import json  # Para manejar el contenido JSON de las credenciales
import firebase_admin  # Para inicializar Firebase
from firebase_admin import credentials, firestore  # Para las credenciales y la conexión a Firestore

# Leer las credenciales desde la variable de entorno
firebase_credentials = os.getenv("FIREBASE_CREDENTIALS")
if not firebase_credentials:
    raise ValueError("La variable de entorno FIREBASE_CREDENTIALS no está configurada.")

# Convertir el JSON de las credenciales a un diccionario
cred_dict = json.loads(firebase_credentials)

# Configurar las credenciales de Firebase
cred = credentials.Certificate(cred_dict)

# Inicializar Firebase
firebase_admin.initialize_app(cred)

# Conectar con Firestore
db = firestore.client()

print("Firebase y Firestore inicializados correctamente.")
