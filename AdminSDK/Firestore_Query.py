import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

emp_ref = db.collection('Employee')

# emp_ref.document('empdoc9').set({
#     'first_name': 'Ian',
#     'last_name': 'Miller',
#     'salary': 800,
#     'status': 'A'
# })

# docs = emp_ref
# docs = docs.where(filter=FieldFilter('first_name', '==', 'Alice')).stream()
#
# for doc in docs:
#     print(doc.to_dict())


emp_ref.where(filter=FieldFilter('salary', '>', 700))
emp_ref.where(filter=FieldFilter('status', '==', 'A'))

docs = emp_ref.get()


for doc in docs:
    print(doc.to_dict())