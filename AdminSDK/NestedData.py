import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference()

data = {
    'users': {
        'user1': {
            'name': 'Alice',
            'email': 'alice@gmail.com',
            'age': 30
        },
        'user2': {
            'name': 'Bob',
            'email': 'bob@gmail.com',
            'age': 35
        },
    }
}

ref.child('nested_data').set(data)