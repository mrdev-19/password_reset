import os
from deta import Deta
from dotenv import load_dotenv

#load env var

load_dotenv(".env")

DETA_KEY=os.getenv("DETA_KEY")
deta=Deta(DETA_KEY)
cred=deta.Base("Creds")
def fetch_all_users():
    res=cred.fetch()
    return res.items

def password_reset(otp,password):
    dev=fetch_all_users()
    usernames=[user["key"] for user in dev]
    emails=[user["email"] for user in dev]
    for user in dev:
        if(user["curkey"]==otp):
            mkey=user["key"]
            change={"curkey":"","password":password}
            cred.update(change,mkey)