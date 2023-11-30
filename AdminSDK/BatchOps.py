import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference()

nested_ref = ref.child('nested_data')

data = {
    'users/user3': {'name': 'Frank', 'email': 'frankie@hld.com', 'age': 28},
    'users/user4': {'name': 'Ottis', 'email': 'ottis@hld.com', 'age': 39},
    'users/user5': {'name': 'Vinnie', 'email': 'vicent@hld.com', 'age': 23}
}

nested_ref.update(data)

