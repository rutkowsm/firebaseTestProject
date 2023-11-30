import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('key.json')
firebase_admin.initialize_app(cred)

# email = input("Please enter an email address: ")
#
# try:
#     user = auth.get_user_by_email(email=email)
#     print(f"User ID: {user.uid}, User email: {user.email}, User phone: {user.phone_number}")
#
# except:
#     print(f"No user found with email {email}")

page = auth.list_users()

for user in page.users:
    print(f"User ID: {user.uid}, User email: {user.email}, User phone: {user.phone_number} "
          f"Verified: {user.email_verified}, Passwd: {user.password_hash}")