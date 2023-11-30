import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

emp_ref = db.reference('Employee')

ref_email = input('Enter email: ')

query = emp_ref.order_by_child('email').equal_to(ref_email).get()

try:
    for user_id, user in query.items():
        name = user.get('name')
        email = user.get('email')
        print(f"User: {user_id}, Name: {name}, email: {email}")
except:
    print(f"No such user with email {ref_email}")