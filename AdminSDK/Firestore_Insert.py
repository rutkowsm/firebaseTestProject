import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('Employee').document('empdoc5')

doc_ref.set({
    'first_name': 'Edward',
    'last_name': 'Mitch',
    'status': 'A'
})