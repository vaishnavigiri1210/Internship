import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- LOAD MODELS ----------------
lr_model = pickle.load(open("lr_model.pkl", "rb"))
log_model = pickle.load(open("log_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Student Predictor", page_icon="🎓")

# ---------------- HEADER ----------------
st.title("🎓 Student Performance Predictor")
st.write("Predict student score and result")

st.markdown("---")

# ---------------- INPUT SECTION ----------------
st.subheader("📥 Enter Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["male", "female"])
    math = st.number_input("Math Score", 0, 100, 50)

with col2:
    reading = st.number_input("Reading Score", 0, 100, 50)
    writing = st.number_input("Writing Score", 0, 100, 50)

test = st.selectbox("Test Preparation", ["none", "completed"])

# Convert categorical
gender = 0 if gender == "male" else 1
test = 0 if test == "none" else 1

input_data = np.array([[gender, math, reading, writing, test]])

st.markdown("---")

# ---------------- PREDICTIONS ----------------
st.subheader("📊 Results")

col1, col2 = st.columns(2)

# 🔵 Score
with col1:
    if st.button("Predict Score"):
        score = lr_model.predict(input_data)
        st.success(f"Average Score: {score[0]:.2f}")

# 🟢 Result
with col2:
    if st.button("Predict Result"):
        input_scaled = scaler.transform(input_data)
        result = log_model.predict(input_scaled)
        prob = log_model.predict_proba(input_scaled)

        if result[0] == 1:
            st.success("PASS ✅")
            st.caption(f"Confidence: {prob[0][1]*100:.1f}%")
        else:
            st.error("FAIL ❌")
            st.caption(f"Confidence: {prob[0][0]*100:.1f}%")

st.markdown("---")

# ---------------- INSIGHT ----------------
avg = (math + reading + writing) / 3

if avg < 50:
    st.warning("Low performance")
elif avg < 70:
    st.info("Average performance")
else:
    st.success("Good performance")

st.markdown("---")

# ---------------- SMALL GRAPH ----------------
st.subheader("📊 Score Comparison")

df = pd.read_csv("StudentsPerformance.csv")

avg_scores = [
    df["math score"].mean(),
    df["reading score"].mean(),
    df["writing score"].mean()
]

subjects = ["Math", "Reading", "Writing"]

fig, ax = plt.subplots(figsize=(5,3))  # 👈 smaller size

ax.bar(subjects, avg_scores, color=["skyblue", "lightgreen", "salmon"])

for i, v in enumerate(avg_scores):
    ax.text(i, v + 1, f"{v:.1f}", ha='center', fontsize=8)

ax.set_title("Avg Scores", fontsize=10)
ax.set_ylabel("Marks", fontsize=9)

st.pyplot(fig)

st.markdown("---")

# ---------------- FOOTER ----------------
st.caption("ML Models: Linear Regression & Logistic Regression")