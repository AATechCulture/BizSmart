import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

load_dotenv()

private_key_path = os.getenv("FIREBASE_KEY_PATH")

if not private_key_path:
    raise ValueError("Private Key not found")

cred = credentials.Certificate(private_key_path)
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://bizsmart-login-default-rtdb.firebaseio.com'
})

class Business:
    name : str
    bType : str
    location : str
    owner : str


    def __init__(self, uuid : str):

     
        ref = db.reference('/users')
        data = ref.get()
        print(data[uuid])

        self.name = data[uuid]['businessName']
        self.bType = data[uuid]['businessType']
        self.location = data[uuid]['location']
        self.owner = data[uuid]['owner']
        