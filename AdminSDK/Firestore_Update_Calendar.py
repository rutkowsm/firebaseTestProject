import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

wkpl_cal_ref = db.collection('Workplace_Calendar').document('HVTG7Z2Cg7GeYgx4xNPL20231204').collection('daily_calendar').document('HVTG7Z2Cg7GeYgx4xNPL20231204').collection('daily_vacancy').document('20231204-01')

wkpl_cal_ref.update({
    'hour_from': 12,
    'hour_to': 20,
    'sequence_number': 1,
    'hour_blocks': {
        '12': {
            'hour_index': 12,
            'covered_by': {
                'employee_id': 'empdoc2',
                'employee_name': 'Bob'
            }
        }
    }
})

# test_ref = db.collection('test_collection').document('4DdBcv3zV0MeVZrauh0D').collection('test_subcollection').document('subdoc1')
#
# test_ref.update({
#     'subfield1': 'gggg'
# })