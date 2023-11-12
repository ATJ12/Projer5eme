import pyrebase 

def database():
    firebaseConfig = {
    "apiKey": "AIzaSyC9tLok-Tc8xadK2ucNHa4KM8sCUv3ITZo",
    "authDomain": "pmbok-fd845-default-rtdb.firebaseio.com",
    "databaseURL": "https://pmbok-fd845-default-rtdb.firebasedatabase.app",
    "projectId": "pmbok-fd845",
    "storageBucket": "pmbok-fd845.appspot.com",
    "messagingSenderId": "6742122919",
    "appId": "1:6742122919:web:c81a75a24a6c2ab7e05682",
    }

    firebase = pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    database = firebase.database()  
    return database 


    


