import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

company_name_input = input("Insert the company name: ")
company_id = input('Set ID: ')
status_input = 'A'

comp_ref = db.collection('Company').document(company_id)

comp_ref.set({
    'name': company_name_input,
    'status': status_input
})

print(f"Company {company_name_input} created")
print("-" * 30)

wkpl_id = input('Set ID: ')
workplace_short_name_input = input("Insert workplace short name: ")
workplace_full_name_input = input("Insert workplace full name: ")
if workplace_full_name_input is None or workplace_full_name_input == '':
    workplace_full_name_input = workplace_short_name_input

workplace_desc_input = input("Insert descritpion: ")

print("-" * 30)
print(f"Set address for premises {workplace_short_name_input}: ")

street_input = input("\tInsert Street name: ")
bld_no_input = input("\tInsert building number: ")
apt_input = input("\tInsert apartment number: ")
postal_code_input = input("\tInsert postal code: ")
add_info_input = input("\tInsert additional info: ")
details_input = input("\tInsert details: ")

address_input = {
    'street': street_input,
    'building_number': bld_no_input,
    'apartment_number': apt_input,
    'postal_code': postal_code_input,
    'additional_info': add_info_input,
    'details': details_input
}

print("-" * 30)
print(f"Set contact details for premises {workplace_short_name_input}: ")

email_input = input("\tInsert email: ")
phone_input = input("\tInsert phone number: ")
www_input = input("\tInsert website: ")

contact_input = {
    'email': email_input,
    'phone_number': phone_input,
    'website': www_input
}

wkpl_ref = db.collection('Company').document(company_id).collection('Workplace').document(wkpl_id)

wkpl_ref.set({
    'short_name': workplace_short_name_input,
    'full_name': workplace_full_name_input,
    'description': workplace_desc_input,
    'status': status_input,
    'address': address_input,
    'contact': contact_input
})

print("-" * 30)

date_input = input('Set date: ')
cal_id = date_input


cal_ref = (db.collection('Company')
           .document(company_id)
           .collection('Workplace')
           .document(wkpl_id)
           .collection('workplace_calendar')
           .document(cal_id))

cal_ref.set({
    'date': date_input,
    'day_index': 1,
    'day_name': 'Monday'
})

print("-" * 30)

seq_no_input = input('Set Sequence Number: ')
vac_id = date_input + '-' + seq_no_input
hour_from_input = input('Set hour from: ')
hour_to_input = input('Set to from: ')

hour_blocks_list = []

hour = int(hour_from_input)
hour_to_int = int(hour_to_input)
while hour < hour_to_int:
    hour_blocks_list.append(hour)
    hour += 1

hour_blocks = {}
for hour in hour_blocks_list:
    hour_str = str(hour)
    hour_blocks[hour_str] = {
        'hour_index': hour,
        'covered_by': {
            'employee_id': None,
            'name': None
        }
    }


vac_ref = (db.collection('Company')
           .document(company_id)
           .collection('Workplace')
           .document(wkpl_id)
           .collection('workplace_calendar')
           .document(cal_id)
           .collection('daily_vacancy')
           .document(vac_id))

cal_ref.set({
    'sequence_number': int(seq_no_input),
    'hour_from': hour_from_input,
    'hour_to': hour_to_input,
    'hour_blocks': hour_blocks
})