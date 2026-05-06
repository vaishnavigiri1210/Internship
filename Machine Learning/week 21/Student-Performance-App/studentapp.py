import streamlit as st
import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("🔥 TEST UPDATE 🔥")

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Student Predictor", page_icon="🎓", layout="centered")

# ---------------- LOAD MODELS ----------------
lr_model = pickle.load(open("lr_model.pkl", "rb"))
log_model = pickle.load(open("log_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# ---------------- TITLE ----------------
st.title("🎓 Student Performance Predictor")
st.caption("Predict average score & pass/fail using ML")

st.markdown("---")

# ---------------- INPUT ----------------
st.subheader("📥 Enter Student Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["male", "female"])
    math = st.number_input("Math Score", 0, 100, 50)

with col2:
    reading = st.number_input("Reading Score", 0, 100, 50)
    writing = st.number_input("Writing Score", 0, 100, 50)

test = st.selectbox("Test Preparation", ["none", "completed"])

# Convert categorical
gender_val = 0 if gender == "male" else 1
test_val = 0 if test == "none" else 1

input_data = np.array([[gender_val, math, reading, writing, test_val]])

st.markdown("---")

# ---------------- PREDICTION ----------------
st.subheader("📊 Prediction Results")

col1, col2 = st.columns(2)

# 🔵 Average Score
with col1:
    if st.button("Predict Score"):
        score = lr_model.predict(input_data)
        st.metric("📘 Average Score", f"{score[0]:.2f}")

# 🟢 Pass/Fail
with col2:
    if st.button("Predict Result"):
        input_scaled = scaler.transform(input_data)
        result = log_model.predict(input_scaled)
        prob = log_model.predict_proba(input_scaled)

        if result[0] == 1:
            st.success("✅ PASS")
            st.caption(f"Confidence: {prob[0][1]*100:.2f}%")
        else:
            st.error("❌ FAIL")
            st.caption(f"Confidence: {prob[0][0]*100:.2f}%")

st.markdown("---")

# ---------------- INSIGHT ----------------
st.subheader("🧠 Performance Insight")

avg_input = (math + reading + writing) / 3

if avg_input < 50:
    st.warning("Low performance")
elif avg_input < 70:
    st.info("Average performance")
else:
    st.success("Good performance")

st.markdown("---")

# ---------------- GRAPH ----------------
st.subheader("📊 Compare with Dataset")

show_graph = st.button("Show Comparison Graph")

if show_graph:

    # safer dataset average
    df["average score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
    ) / 3

    avg_dataset = df["average score"].mean()

    chart_df = pd.DataFrame({
        "Category": ["Your Score", "Dataset Avg"],
        "Score": [avg_input, avg_dataset]
    })

    fig, ax = plt.subplots(figsize=(4,3))

    sns.barplot(
        x="Category",
        y="Score",
        data=chart_df,
        ax=ax
    )

    # labels on bars
    for i, v in enumerate(chart_df["Score"]):
        ax.text(i, v + 1, f"{v:.1f}", ha='center', fontsize=9)

    ax.set_title("Score Comparison")
    ax.set_ylim(0, 100)

    st.pyplot(fig)

st.markdown("---")

# ---------------- FOOTER ----------------
st.caption("⚙️ Models: Linear Regression (Score) + Logistic Regression (Pass/Fail)")