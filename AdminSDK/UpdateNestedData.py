import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference()

nested_ref = ref.child('nested_data')

nested_ref.child('users/user1/age').set(32)

nested_ref.update({
    'users/user2/name': 'Robert',
    'users/user2/email': 'robert@company.com'
})

