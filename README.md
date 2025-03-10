# TrustTelecom Churn Prediction Web App

### Predicting Customer Churn with Machine Learning

This repository contains the **TrustTelecom Churn Prediction Tool**, a Flask-based web application that predicts the likelihood of customer churn using a machine learning model. The tool is designed to help customer service teams identify high-risk customers and take proactive measures to improve retention.

## 📌 Project Overview
- **Framework:** Flask (Python)
- **Deployment:** Hosted on an **AWS EC2 instance** with **Docker** containerisation
- **Model Used:** Random Forest Classifier (Fine-tuned with hyperparameter optimisation)
- **Evaluation Metric:** **AUC (Area Under the Curve) Score**

---

## 👨‍💻 Author
Rui Xin Oh

---

## 🌍 Live Web Application
**URL:** [Deployed Flask App](https://your-deployed-url.com)  
*(Click the link above to access the live web application)*

---

## 🏆 Final Model Details

- **Chosen Model:** `RandomForestClassifier`
- **Hyperparameters:**
  - `n_estimators`: **200**
  - `min_samples_split`: **10**
  - `min_samples_leaf`: **1**
  - `max_features`: **'log2'**
  - `max_depth`: None
  - `bootstrap`: **True**
- **Offline AUC Score:** **0.8472** *(on test dataset)*
- **Feature Selection:** Used **SHAP (SHapley Additive exPlanations)** to refine input features

---

## 💻 Running the Project Locally

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/trusttelecom-churn-prediction.git
cd trusttelecom-churn-prediction
