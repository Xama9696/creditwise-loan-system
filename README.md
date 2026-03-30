# 💳 CreditWise Loan Approval & Risk Monitoring System

This project is an end-to-end credit risk analytics system that simulates how banks evaluate loan applications, monitor model outputs, and generate insights.

A machine learning model predicts loan approval using features like income, credit score, and engineered metrics such as debt-to-income ratio. The model is deployed via a Streamlit app, allowing users to input details and receive instant decisions.

To mimic real-world systems, all predictions are logged with timestamps, enabling basic monitoring and traceability. A Tableau dashboard complements the system by visualizing approval trends, income vs loan patterns, and credit risk insights.

Together, the application and dashboard demonstrate both the operational and analytical aspects of modern banking data systems.
---

## 🛠️ Technologies Used

Python, Pandas, NumPy, Scikit-learn, Streamlit, Tableau, Pickle

---

## 📂 Project Structure

creditwise-loan-system/

- app.py → Streamlit application for prediction and logging  
- credit_wise.ipynb → Model training and data analysis  
- model.pkl → Trained machine learning model  
- loan_approval_data.csv → Dataset  
- prediction_log.csv → Generated logs for monitoring  
- requirements.txt  

---

## ⚙️ Running the Application

Install dependencies and run the Streamlit app:

pip install -r requirements.txt  
streamlit run app.py  

---

## 📊 Outputs

The system produces two key outputs:

1. A live application that predicts loan approval and logs each prediction  
2. A dashboard that visualizes approval trends, income patterns, and credit risk insights  



---

## 🧠 Key Learnings

This project demonstrates how machine learning models move beyond training into real-world usage. It highlights the importance of model monitoring, logging, and visualization in building reliable data systems, especially in financial domains where decision accuracy and transparency are critical.

---

## 👤 Author  
Mohammad Zaman Asif
