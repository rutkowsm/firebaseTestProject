import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

emp_ref = db.reference('Employee')

employees = emp_ref.get()
total_employees = len(employees)
print(f"Total number of employees: {total_employees}")
