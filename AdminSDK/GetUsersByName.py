import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

emp_ref = db.reference('Employee')

query = emp_ref.order_by_child('name').start_at('B').end_at('B\uf8ff').get()
for emp_id, employee in query.items():
    name = employee.get('name')
    email = employee.get('email')
    print(f"Employee ID: {emp_id}; Name: {name}; Email: {email}")