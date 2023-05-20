import streamlit as st
import database as db
import validations as val
import hasher as hs
#---------------------------------------------------
# page config settings:

page_title="Reset Password"
page_icon=":key:"
layout="centered"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)

#--------------------------------------------------
#hide the header and footer     

hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)

with st.form("Password Reset",clear_on_submit=False):
    otp=st.text_input("Enter the OTP recieved")
    newpass=st.text_input("Enter your password")
    submit=st.form_submit_button()
    if(submit):
        if(val.validate_password(newpass)):
            newpass=hs.hasher(newpass)
            db.password_reset(otp,newpass)
            st.success("Password Reset Successfully!")
        else:
            st.error("Password must be between 6-20 characters in length and must have at least one Uppercase Letter , Lowercase letter , numeric character and A Special Symbol(#,@,$,%,^,&,+,=)")
