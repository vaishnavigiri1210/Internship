import streamlit as st
import pickle
import numpy as np

# Title
st.title("Customer Churn Prediction")

# Load saved model
model = pickle.load(open('model.pkl', 'rb'))

# User inputs
tenure = st.number_input("Enter Tenure (months)")
monthly_charges = st.number_input("Enter Monthly Charges")

# Predict button
if st.button("Predict"):
    
    # Input convert to array
    data = np.array([[tenure, monthly_charges]])
    
    # Prediction
    result = model.predict(data)
    
    if result[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will NOT churn ✅")