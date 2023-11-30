import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference('Employee')

users = ref.get()

for user_id, user in users.items():
    name = user.get('name')
    email = user.get('email')
    print(f"User: {user_id}, Name: {name}, email: {email}")