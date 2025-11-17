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
```python
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(scaler, open("scaler.pkl", "wb"))
