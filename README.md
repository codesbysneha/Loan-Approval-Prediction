# 🏦 Loan Approval Prediction – End-to-End Machine Learning Project

This project is an end-to-end Machine Learning system that predicts whether a loan application should be **Approved** or **Rejected** based on key financial features such as **Annual Income** and **Credit Score**.  
The project demonstrates every step of the ML lifecycle — from data preprocessing to deployment.

---

## 🚀 **Project Workflow**

### **1️⃣ Data Collection**
A custom dataset (`loan_data.csv`) is used containing:
- Annual Income  
- Credit Score  
- Loan Approval Status (0 = Rejected, 1 = Approved)

---

### **2️⃣ Exploratory Data Analysis (EDA)**
- Data cleaning  
- Visualizing relationships (scatter plots)  
- Understanding the distribution of features  

---

### **3️⃣ Data Preprocessing**
- Feature selection  
- Train-test split  
- Standardization using **StandardScaler**  
- Converting values into ML-ready format  

---

### **4️⃣ Model Building**
The project uses **Logistic Regression**, a simple yet powerful model for binary classification.

Steps include:
- Training the model  
- Evaluating accuracy  
- Visualizing decision boundaries  

---


### **5️⃣ Saving the Model**
The trained model and scaler are saved using:
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))


6️⃣ Deployment Using Streamlit

A user-friendly web interface is created where users can enter:

Annual Income

Credit Score

The app then predicts:
✔ Loan Approved
❌ Loan Rejected

The app is run using:
streamlit run app.py


In Google Colab, ngrok is used to expose the app online.
🛠️ Tech Stack
   Python
   NumPy
   Pandas
   Scikit-Learn
   Streamlit
   Ngrok
  Matplotlib

📊 Model Accuracy
Final test accuracy: ~90%
(Varies based on random train-test split)

✨ Features
End-to-end ML pipeline
Clean and simple UI
Real-time predictions
Lightweight and easy to deploy
Beginner-friendly workflow


