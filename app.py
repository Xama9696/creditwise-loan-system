import streamlit as st
import pickle
import numpy as np
import pandas as pd
import datetime

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("CreditWise Loan Approval System")

# ----------- INPUTS -----------

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
age = st.number_input("Age", min_value=18, max_value=100)
dependents = st.number_input("Dependents", min_value=0, max_value=10)
existing_loans = st.number_input("Existing Loans", min_value=0)
savings = st.number_input("Savings", min_value=0)
collateral_value = st.number_input("Collateral Value", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (months)", min_value=0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850)

education = st.selectbox("Education Level", ["High School", "Bachelor", "Master", "PhD"])
employment_status = st.selectbox("Employment Status", ["Business", "Salaried", "Self-employed", "Unemployed"])
marital_status = st.selectbox("Marital Status", ["Married", "Single"])
loan_purpose = st.selectbox("Loan Purpose", ["Business", "Car", "Education", "Home", "Personal"])
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
gender = st.selectbox("Gender", ["Female", "Male"])
employer_category = st.selectbox("Employer Category", ["Business", "Government", "MNC", "Private", "Unemployed"])

# ----------- PREDICT -----------

if st.button("Predict"):

    # Feature Engineering
    dti_ratio = loan_amount / (applicant_income + 1)
    dti_ratio_sq = dti_ratio ** 2
    credit_score_sq = credit_score ** 2

    education_map = {"High School": 0, "Bachelor": 1, "Master": 2, "PhD": 3}
    education_encoded = education_map[education]

    features = {
        'Applicant_Income': applicant_income,
        'Coapplicant_Income': coapplicant_income,
        'Age': age,
        'Dependents': dependents,
        'Existing_Loans': existing_loans,
        'Savings': savings,
        'Collateral_Value': collateral_value,
        'Loan_Amount': loan_amount,
        'Loan_Term': loan_term,
        'Education_Level': education_encoded,
        'Employment_Status_Salaried': 1 if employment_status == "Salaried" else 0,
        'Employment_Status_Self-employed': 1 if employment_status == "Self-employed" else 0,
        'Employment_Status_Unemployed': 1 if employment_status == "Unemployed" else 0,
        'Marital_Status_Single': 1 if marital_status == "Single" else 0,
        'Loan_Purpose_Car': 1 if loan_purpose == "Car" else 0,
        'Loan_Purpose_Education': 1 if loan_purpose == "Education" else 0,
        'Loan_Purpose_Home': 1 if loan_purpose == "Home" else 0,
        'Loan_Purpose_Personal': 1 if loan_purpose == "Personal" else 0,
        'Property_Area_Semiurban': 1 if property_area == "Semiurban" else 0,
        'Property_Area_Urban': 1 if property_area == "Urban" else 0,
        'Gender_Male': 1 if gender == "Male" else 0,
        'Employer_Category_Government': 1 if employer_category == "Government" else 0,
        'Employer_Category_MNC': 1 if employer_category == "MNC" else 0,
        'Employer_Category_Private': 1 if employer_category == "Private" else 0,
        'Employer_Category_Unemployed': 1 if employer_category == "Unemployed" else 0,
        'DTI_Ratio_sq': dti_ratio_sq,
        'Credit_Score_sq': credit_score_sq,
    }

    input_df = pd.DataFrame([features])

    # Prediction
    result = model.predict(input_df)

    # Display result
    if result[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    # ----------- LOGGING -----------

    log_data = input_df.copy()
    log_data["prediction"] = result[0]
    log_data["timestamp"] = datetime.datetime.now()

    log_data.to_csv("prediction_log.csv", mode='a', header=False, index=False)

# ----------- VIEW LOGS -----------

if st.sidebar.button("View Logs"):
    try:
        logs = pd.read_csv("prediction_log.csv")
        st.write(logs.tail(20))
    except:
        st.write("No logs available yet")
