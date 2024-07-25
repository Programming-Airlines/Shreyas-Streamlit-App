import streamlit as st
import pandas as pd

st.title("My Enjoyability of my Chosen Subjects for GCSE")
data = pd.read_csv('Subject Enjoyability.csv')
st.bar_chart(data.groupby('Subject')['Enjoyability'].sum())