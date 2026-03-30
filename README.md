# 💳 CreditWise Loan Approval & Monitoring System

## 🚀 Overview
This project is an end-to-end **credit risk prediction and monitoring system** built using Machine Learning and deployed with Streamlit.

It not only predicts loan approval decisions but also simulates **real-world model monitoring** used in banking systems by logging predictions and tracking model behavior.

---

## 🎯 Features

- 🔍 Loan approval prediction using Machine Learning  
- 📊 Interactive web application using Streamlit  
- 📝 Prediction logging system (stored in CSV)  
- ⚙️ Feature engineering (DTI ratio, credit score transformations)  
- 📈 Basic monitoring pipeline for tracking model outputs  

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit**
  

---

## 📂 Project Structure
creditwise-loan-system/
│
├── app.py # Streamlit application
├── credit_wise.ipynb # Model training & EDA
├── model.pkl # Trained ML model
├── loan_approval_data.csv # Dataset
├── prediction_log.csv # Generated logs
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. User inputs loan applicant details  
2. Model predicts approval (Yes/No)  
3. Input + prediction is logged with timestamp  
4. Logs can be viewed inside the app  

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py


Dashboard (Tableau)

This project also includes a Tableau dashboard analyzing:

Loan approval distribution
Income vs loan amount patterns
Credit score comparison
