from decouple import config
from firebase_admin import credentials, initialize_app

# Inicializa Firebase usando la ruta especificada en el .env
def init_firebase():
    firebase_key_path = config("FIREBASE_KEY_PATH")  # Lee la variable del archivo .env
    cred = credentials.Certificate(firebase_key_path)
    initialize_app(cred)
    print("Firebase inicializado correctamente")
