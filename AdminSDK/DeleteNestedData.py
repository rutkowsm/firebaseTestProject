import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference()

nested_ref = ref.child('nested_data')

# nested_ref.child('users/user2').delete()

nested_ref.delete()