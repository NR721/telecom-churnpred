# TrustTelecom Churn Prediction Web App

### Predicting Customer Churn with Machine Learning

This repository contains the **TrustTelecom Churn Prediction Tool**, a Flask-based web application that predicts the likelihood of customer churn using a machine learning model. The tool is designed to help customer service teams identify high-risk customers and take proactive measures to improve retention.

## 📌 Project Overview
- **Framework:** Flask (Python)
- **Deployment:** Hosted on an **AWS EC2 instance** with **Docker** containerisation
- **Model Used:** Random Forest Classifier (Fine-tuned with hyperparameter optimisation)
- **Evaluation Metric:** **AUC (Area Under the Curve) Score**

---

## Author
Rui Xin Oh

---

## Live Web Application
**URL:** [Deployed Flask App](http://ec2-18-116-49-118.us-east-2.compute.amazonaws.com/)  
*(Click the link above to access the live web application)*

---

## Final Model Details

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

### **Clone the Repository**
```bash
git clone https://github.com/Heicoders-AI300/jan25-p01.git
cd trusttelecom-churn-prediction
```

### **Prerequisites**
Before installing Python dependencies, install system dependencies:

```bash
# For macOS (Homebrew)
brew install cmake ninja llvm
brew install python@3.10

# For Ubuntu/Debian
sudo apt update && sudo apt install cmake ninja-build llvm
```

### **Set Up a Virtual Environment**
```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Run Flask Application**
```bash
python src/app.py
```
Your app should now be running at **http://localhost:5000/**.

---

## 🛠️ API Endpoints
| Method | Endpoint         | Description |
|--------|-----------------|-------------|
| `POST` | `/api_json`      | Get churn prediction via API |
| `GET`  | `/cust_churn_pred` | Render the customer prediction form |
| `GET`  | `/file`          | Download model file |

---

## 🐳 Docker Deployment
If using Docker for containerised deployment, follow these steps:

### **Build the Docker Image**
```bash
docker build -t rxoh/trusttelecom-churn-app:1.1  .
```

### **Run the Container**
```bash
docker run -d -p 80:80 rxoh/trusttelecom-churn-app:1.1  .
```
