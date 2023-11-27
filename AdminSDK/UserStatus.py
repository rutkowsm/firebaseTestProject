import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

email = input("Please enter an email address: ")

try:
    user = auth.get_user_by_email(email=email)
    user_status = 'Active'
    if user.disabled:
        user_status = 'Inactive'
    print(f"User ID: {user.uid}, User status: {user_status}")

except:
    print(f"No user found with email {email}")