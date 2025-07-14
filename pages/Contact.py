import streamlit as st

st.title("Contact")

#name email  phone number button
#
#

first_name=st.text_input("Enter your first name")
last_name=st.text_input("Enter your last name")
email=st.text_input("Enter your email")
phone_number=st.text_input("Enter your phone number")
if st.button("Submit"):
    print(f"Thank you {first_name} {last_name} for your input")
else:
    pass

enquiries=st.text_area("Enter your enquiries")
st.write(enquiries)

documents= st.file_uploader("upload your files")