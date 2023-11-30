import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

emp_ref = db.collection('Employee')

docs = emp_ref.stream()

# for doc in docs:
#     print("{} => {}".format(doc.id, doc.to_dict()))

for doc in docs:
    print(f"{doc.id}: {doc.to_dict()}")