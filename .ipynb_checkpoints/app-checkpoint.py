import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("CreditWise Loan Approval System")

income = st.number_input("Annual Income")
age = st.number_input("Age")
loan_amount = st.number_input("Loan Amount")
credit_score = st.number_input("Credit Score")

if st.button("Predict"):
    features = np.array([[income, age, loan_amount, credit_score]])
    result = model.predict(features)
    st.write("✅ Loan Approved" if result[0] == 1 else "❌ Loan Rejected")