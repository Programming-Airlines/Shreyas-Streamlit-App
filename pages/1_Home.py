import streamlit as st
import time

def stream_data():
    with st.expander("Discover Me"):
        _Website_Welcoming = """Hi! I am Shreyas! Welcome to my website. I am an avid cyber security enthusiast studying in London, UK. I am a Year 9 High School Student."""
        for word in _Website_Welcoming.split(" "):
            yield word + " "
            time.sleep(0.1)

st.title("About Shreyas")
if st.button("Delve More About Me"):
    st.write(" ".join(list(stream_data())))