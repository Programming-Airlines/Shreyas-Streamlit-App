'''import streamlit as st
import time
import numpy as np
import pandas as pd

_Website_Welcoming = """Hi! I am Shreyas! Welcome to my website. I am an avid cyber security interest studying in London, UK. I am a Year 9 High School Student"""
st.balloons()
st.title("About Shreyas")
def stream_data():
  for word in _Website_Welcoming.split(" "):
    yield word + " "
    time.sleep(0.1)
pg = st.sidebar.selectbox("Select a Page", ["Home", "My Interests (Subjects)", "Physical Appearance"])
if pg == "Home":
  if st.button("Delve More About Me"):
    st.write_stream(stream_data)
elif pg == "My Interests Ranked(Subjects)":
  st.write("This page will show my subject interests")
  st.title("My Enjoyability of my Chosen Subjects for GCSE")
  data = pd.read_csv('Subject Enjoyability.csv')
  st.bar_chart(data.groupby('Subject')['Enjoyability'].sum())
elif pg == "Physical Appearance":
  st.write("This page will have my physical appearance in photos")
  st.image("Shreyas Pic1.png", width=200)
  st.image("Shreyas Pic2.png", width=200)
  st.image("Shreyas Pic3.png", width=200)
  st.image("Shreyas Pic4.png", width=200)'''