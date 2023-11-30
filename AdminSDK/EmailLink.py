import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

email = input("Please enter an email address: ")

try:
    # link = auth.generate_email_verification_link(email)
    link = auth.generate_password_reset_link(email)
    print(link)
except:
    print(f"No user found with email {email}")

