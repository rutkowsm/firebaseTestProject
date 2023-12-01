import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def on_collection_update(col_shapshot, changes, read_time):
    for change in changes:
        if change.type.name == 'ADDED':
            print("New document added")
            print(change.document.to_dict())
            print("-" * 15)
        elif change.type.name == 'MODIFIED':
            print(f"Document {change.document.id} updated")
            print(change.document.to_dict())
            print("-" * 15)
        elif change.type.name == 'REMOVED':
            print(f"Document {change.document.id} deleted")
            print(change.document.to_dict())
            print("-" * 15)


col_ref = db.collection('Employee')
col_watch = col_ref.on_snapshot(on_collection_update)

while True:
    pass
