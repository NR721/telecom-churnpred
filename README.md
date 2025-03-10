# 📊 TrustTelecom Churn Prediction Web App

### 🚀 Predicting Customer Churn with Machine Learning

This repository contains the **TrustTelecom Churn Prediction Tool**, a Flask-based web application that predicts the likelihood of customer churn using a machine learning model. The tool is designed to help customer service teams identify high-risk customers and take proactive measures to improve retention.

## 📌 Project Overview
- **Framework:** Flask (Python)
- **Deployment:** Hosted on an **AWS EC2 instance** with **Docker** containerisation.
- **Model Used:** Random Forest Classifier (Fine-tuned with hyperparameter optimisation)
- **Evaluation Metric:** **AUC (Area Under the Curve) Score**

---

## 👨‍💻 Authors
- **[Your Full Name]** (Primary Author)
- **[Collaborator’s Name, if applicable]**

---

## 🌍 Live Web Application
🔗 **URL:** [Deployed Flask App](https://your-deployed-url.com)  
*(Click the link above to access the live web application.)*

---

## 🏆 Final Model Details

- **Chosen Model:** `RandomForestClassifier`
- **Hyperparameters:**
  - `n_estimators`: **500**
  - `max_depth`: **15**
  - `min_samples_split`: **5**
  - `min_samples_leaf`: **2**
  - `max_features`: **'sqrt'**
  - `bootstrap`: **True**
- **Offline AUC Score:** **0.89** *(on test dataset)*
- **Feature Selection:** Used **SHAP (SHapley Additive exPlanations)** to refine input features.

---

## 💻 Running the Project Locally

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/trusttelecom-churn-prediction.git
cd trusttelecom-churn-prediction
