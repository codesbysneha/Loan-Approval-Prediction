import streamlit as st
import pickle
import numpy as np

# Load model & scaler
with open('/content/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('/content/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

st.set_page_config(page_title="Loan Approval Predictor", layout="centered")
st.title("Loan Approval Prediction App")
st.markdown("Enter applicant details and click **Predict** to see if the loan is likely to be approved.")

income = st.number_input("Enter Annual Income (₹)", min_value=10000, max_value=1000000, value=50000, step=1000)
credit_score = st.number_input("Enter Credit Score", min_value=300, max_value=900, value=600, step=1)

if st.button("Predict"):
    data = np.array([[income, credit_score]])
    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)

    if int(prediction[0]) == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
