import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate('../privateKey/raspberryfirebase-firebase-adminsdk-q4ht6-92b0f0e25f.json');
default_app = firebase_admin.initialize_app(cred);

#detrieve user data
user = auth.get_user('hRyeR48vItYinv4NzcEjxLrC0Ew1');
print('custom_claims:',user.custom_claims);

print(default_app.name);