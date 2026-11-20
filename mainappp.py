import streamlit as st
st.title("Discipline and movitated")
st.header("wallpaper")
name=st.text_input("enter your name")
age=st.number_input("enter your age",min_value=18,max_value=100,step=5)
st.write(f"name{name} your age is {age}")
gender=st.selectbox("select your gender",["Male","Female"])
subject=st.multiselect("select your choice",["Python","java","c++","mysql"])
login=st.button("login")

if login:
    st.success("submitted sucessfully")
    st.write(name)
    st.write(age)
    st.write(gender)
    st.write(subject)

st.divider()
#st.image(r"C:\Users\OWAIS AHMAD\OneDrive\Pictures\WhatsApp Image 2026-11-19 at 11.54.37 AM.jpeg")
import os
st.image(os.path.join(os.getcwd(),"static","babar.jpg"))