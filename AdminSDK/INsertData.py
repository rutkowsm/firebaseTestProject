import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

#insert data

# emp_name = input("Enter your name: ")
# emp_email = input("Enter your email address: ")
# emp_phone = input("Enter your phone number: ")
# print("Enter your address:")
# emp_street = input("\tStreet: ")
# emp_str_number = input("\tBuilding number: ")
# emp_apt_number = input("\tApartment number: ")


# ref = db.reference(('/'))
#
# ref.set({
#     'Employee': {
#         # 'emp1': {
#         #     'name': emp_name,
#         #     'email': emp_email,
#         #     'address': {
#         #         'street': emp_street,
#         #         'number': emp_str_number,
#         #         'apt': emp_apt_number
#         #     }
#         # },
#         'emp1': {
#             'name': 'Bob',
#             'email': 'bob@company.com',
#             'address': {
#                 'street': 'Sienkiewicza',
#                 'number': '44b',
#                 'apt': 12
#             }
#         },
#         'emp2': {
#             'name': 'Zenon',
#             'email': 'zenon@piwoni.pl',
#             'address': {
#                 'street': 'Ks. Witolda',
#                 'number': '14',
#                 'apt': '20'
#             }
#         },
#     }
# })

ref = db.reference(('Employee'))

emp_ref = ref.push({
    'name': 'Chandler',
    'email': 'chandler@bing.com',
    'address': {
        'street': 'Grunwaldzka',
        'number': '144f',
        'apt': 66
    }
})