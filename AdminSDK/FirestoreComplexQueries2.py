import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

status_search = "A"

query = db.collection('Employee').where(filter=FieldFilter('status', '==', status_search))

results = query.get()

print(f"{len(results)} employees match your result")
print("-" * 15)

for doc in results:
    print(f"Emp ID: {doc.id}")
    print(f"Emp ID: {doc.get('first_name')}")
    print(f"Emp ID: {doc.get('last_name')}")
    # print(f"Emp ID: {doc.get('salary')}")
    print(f"Emp ID: {doc.get('status')}")
    print("-" * 15)