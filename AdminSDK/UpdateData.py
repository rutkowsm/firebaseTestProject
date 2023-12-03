import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

ref = db.reference('Employee')

emp_ref = ref.child('emp2')

emp_ref.update({
    'email': 'zenek@company.com'
})


