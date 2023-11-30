import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference('')

nested_ref = ref.child('nested_data')

user1_name = nested_ref.child('users/user1/name').get()
user1_email = nested_ref.child('users/user1/email').get()

print(f"{user1_name}; {user1_email}")