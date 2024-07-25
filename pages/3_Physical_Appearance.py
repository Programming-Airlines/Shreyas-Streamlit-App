import streamlit as st
import time

st.title("My Physical Appearance")
st.write("This page will have my physical appearance in photos")
progress_text = "Images casually loading. Please wait..."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()
st.image("streamlitPractice/Shreyas Pic1.png", width=200)
time.sleep(10)
st.image("streamlitPractice/Shreyas Pic2.png", width=200)
time.sleep(10)
st.image("streamlitPractice/Shreyas Pic3.png", width=200)
time.sleep(10)
st.image("streamlitPractice/Shreyas Pic4.png", width=200)
