import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myproject-ab437-default-rtdb.firebaseio.com/'
})

emp_ref = db.reference('Employee')

# name_input = input("Enter name for search: ")
# filtered_employees = emp_ref.order_by_child('name').equal_to(name_input).get()
#
# try:
#     for emp_id, employee in filtered_employees.items():
#         print(f"Employee ID: {emp_id}")
#         print(f"Name: {employee['name']}; Email: {employee['email']}")
#
# except:
#     print(f"No employee with name: {name_input}")

sorted_emps = emp_ref.order_by_child('name').get()

for emp_id, employee in sorted_emps.items():
    print(f"Employee ID: {emp_id}")
    print(f"Name: {employee['name']}; Email: {employee['email']}")