import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt

# Title and Headers
st.title("Streamlit UI Showcase")
st.header("Welcome to the Interactive UI Elements")

# Text Elements
st.subheader("Basic Text Elements")
st.write("Hello")
st.write("Ritesh")

# Data Display
st.subheader("Displaying Data from Groww")
df = pd.read_html('https://groww.in/gold-rates')[0]
st.dataframe(df)

# User Inputs
st.subheader("User Input Widgets")
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100, value=25)
option = st.selectbox("Select an option:", ["Option 1", "Option 2", "Option 3"])
checkbox = st.checkbox("Check this box")
button = st.button("Submit")
if button:
    st.write(f"Hello {name}, you selected {option} and checked: {checkbox}")

# Sidebar
st.sidebar.title("Sidebar Navigation")
page = st.sidebar.radio("Go to", ["Home", "Charts", "Tables"])

# Charts
st.subheader("Random Data Chart")
data = np.random.randn(100, 2)
df_chart = pd.DataFrame(data, columns=["X", "Y"])
st.line_chart(df_chart)

# Progress Bar
st.subheader("Progress Bar")
import time
progress_bar = st.progress(0)
for i in range(101):
    time.sleep(0.01)
    progress_bar.progress(i)

# File Upload
st.subheader("File Upload")
uploaded_file = st.file_uploader("Upload a file")
if uploaded_file:
    st.write("File uploaded successfully!")
