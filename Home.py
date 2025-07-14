import streamlit as st
import time


sign_up= st.button('Sign Up ')
if sign_up:
    @st.dialog("Sign Up")
    def signup():
        username = st.text_input("Enter your username")
        phone_number = st.text_input("Enter your phone number")

        if st.button("Sign Up save"):
            st.write(f"{username} has signed up!")


    signup()

st.title("this is a title")
st.header("this is a header")
st.subheader("this is a subheader")
st.write("hello world")
st.caption("this is a caption")

st.code("""

import streamlit as st

st.title("this is a title")
st.header("this is a header")
st.subheader("this is a subheader")
st.write("hello world")
st.caption("this is a caption")
""")

with st.echo():
    st.write("this code will be executed")

st.divider()

st.subheader("this is section 2")

st.write("------------")

user_feedback=st.feedback()
if user_feedback == 0:
    st.write("thank u for ur feedback we appreciate your feedback ")
elif user_feedback == 1:
    st.write("ok.thanks for ur feedback we will strive to improve ")
else:
    pass

stars_feedback = st.feedback("stars")
st.write(stars_feedback)
if stars_feedback == 0:
    st.write("the number of stars u have selected is 1")
elif stars_feedback == 1:
    st.write("the number of stars u have selected is 2")
elif stars_feedback == 2:
    st.write("the number of stars u have selected is 3")
elif stars_feedback == 3:
    st.write("the number of stars u have selected is 4")
elif stars_feedback == 4:
    st.write("the number of stars u have selected is 5")
else:
    pass


dark_mode = st.toggle("Dark mode")
if dark_mode:
    st.caption("** Dark mode has been turned on **")

user_checkbox = st.checkbox("I agree to the terms of use")
if user_checkbox:
    st.caption("I agree to the terms of use")

st.metric("Temperature", 20, -2)

st.metric("Rainfall", 1200, 120)

st.button("submit")

st.button("post")


# categorical user inputs

st.radio("select your gender",["Male","Female"])

favourite_team=st.selectbox("select your favourite team",["ARSENAL","CHELSEA","MAN-CITY","MAN-U"])
if favourite_team == "ARSENAL":
    st.write("london is red")
elif favourite_team == "CHELSEA":
    st.write("london is blue")
elif favourite_team == "MAN-CITY":
    st.write("Manchester is blue")
elif favourite_team == "MAN-U":
    st.write("Manchester is red")


breakfast= st.multiselect("what did u have for breakfast",["Tea", "Coffee","Hot Chocolate" ])

st.write(breakfast)

st.select_slider("enter the size of your t-shirt",["small","medium","large"])

st.code("**you're prompt for Gemini api will go here**")

st.write("-------------")

st.metric("Average Performance",380 ,30)

st.write("--------------")

st.checkbox("Are you a student?")

st.write("-------------")

blood_group=st.radio("select your blood type",["A","B","AB","O"])
rhesus_factor=st.toggle("rhesus factor")
if rhesus_factor:
    rhesus_factor_user= "+"
else:
    rhesus_factor_user= "-"
full_blood_type =f"{blood_group}{rhesus_factor_user}"
st.write(full_blood_type)
st.write("--------------")

user_select_box=st.selectbox("Choose you're lab",["Lab 1","Lab 2","Lab 3","Lab 4"])
if user_select_box == "Lab 1":
    st.write("lab 1")
elif user_select_box == "Lab 2":
    st.write("lab 2")
elif user_select_box == "Lab 3":
    st.write("Lab 3")
elif user_select_box == "Lab 4":
    st.write("Lab 4")


st.write("--------------")

st.select_slider("enter the level of your education",["early childhood education", "primary education", "secondary education","higher education"])

st.write("--------------")

st.number_input("Enter your age",1, 100, 26)
st.slider("Enter your weight",10,200,50)

st.write("--------------")

appointment_date=st.date_input("Enter your appointment date")
appointment_time=st.time_input("Enter your appointment time")

st.write("--------------")

first_name=st.text_input("Enter your first name")
last_name=st.text_input("Enter your last name")
email=st.text_input("Enter your email")
if st.button("Save Details"):
    st.write(f"Welcome {first_name} {last_name}")

st.text_area("enter your essay here:", height= 200)

st.write("--------------")


uploaded_file=st.file_uploader("Upload File")

st.camera_input("Take a photo of your self")
st.image("test.jpg")

photo_taken=st.camera_input("Take a photos of your self")
if photo_taken:
  st.image(photo_taken, width=200)

st.write("--------------")

col1,col2 = st.columns(2)
with col1:
    st.text_input("Enter your first name", max_chars=30)
with col2:
    st.text_input("Enter your last name", max_chars=30)


st.write("---------")

with st.expander("Click to see more details"):
    st.write("details")
    st.write("details")
    st.write("details")
    st.write("details")
    st.write("details")
    st.write("details")
    st.write("details")
    st.write("details")

st.write("--------------")

with st.sidebar:
    st.write("Welcome back")

st.write("--------------")

with st.spinner("Spider Spider"):
    time.sleep(5)

st.write("------")

st.toast("welcome", icon="👍")

st.write("--------")

st.balloons()

st.write("--------")

st.success("success")
st.info("info")
st.warning("warning")
st.error("error")