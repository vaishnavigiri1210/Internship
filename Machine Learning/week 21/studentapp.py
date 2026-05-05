import streamlit as st
import numpy as np
import pickle

# Load model (make sure model.pkl is in same folder)
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🎓 Student Performance Prediction")

st.write("Enter student details to predict average score")

# Input fields
gender = st.selectbox("Gender", ["male", "female"])
math = st.number_input("Math Score")
reading = st.number_input("Reading Score")
writing = st.number_input("Writing Score")
test = st.selectbox("Test Preparation", ["none", "completed"])

# Convert text to number
gender = 0 if gender == "male" else 1
test = 0 if test == "none" else 1

# Predict button
if st.button("Predict"):
    input_data = np.array([[gender, math, reading, writing, test]])

    prediction = model.predict(input_data)

    st.success(f"Predicted Average Score: {prediction[0]}")