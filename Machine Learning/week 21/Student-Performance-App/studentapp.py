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

# Load dataset once
df = pd.read_csv("StudentsPerformance.csv")

# ---------------- UI ----------------
st.set_page_config(page_title="Student Predictor", page_icon="🎓")

st.title("🎓 Student Performance Predictor")
st.write("Enter student details to predict performance")

st.markdown("---")

# ---------------- INPUT ----------------
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

# ---------------- PREDICTION ----------------
st.subheader("📊 Results")

col1, col2 = st.columns(2)

# Score Prediction
with col1:
    if st.button("Predict Score"):
        score = lr_model.predict(input_data)
        st.metric("Average Score", f"{score[0]:.2f}")

# Pass/Fail
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
avg_input = (math + reading + writing) / 3

if avg_input < 50:
    st.warning("Low performance")
elif avg_input < 70:
    st.info("Average performance")
else:
    st.success("Good performance")

st.markdown("---")

# ---------------- DYNAMIC GRAPH ----------------
st.subheader("📊 Compare Your Score")

if st.button("Show Comparison Graph"):

    avg_dataset = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
    ).mean() / 1  # already mean of total

    chart_df = pd.DataFrame({
        "Type": ["Your Score", "Dataset Average"],
        "Score": [avg_input, avg_dataset]
    })

    fig, ax = plt.subplots(figsize=(4,3))

    sns.barplot(
        x="Type",
        y="Score",
        data=chart_df,
        ax=ax,
        palette=["skyblue", "lightgreen"]
    )

    for i, v in enumerate(chart_df["Score"]):
        ax.text(i, v + 1, f"{v:.1f}", ha='center', fontsize=9)

    ax.set_title("Your Score vs Dataset Average", fontsize=10)
    ax.set_ylabel("Marks")

    st.pyplot(fig)

st.markdown("---")

# ---------------- FOOTER ----------------
st.caption("ML Models: Linear Regression & Logistic Regression")