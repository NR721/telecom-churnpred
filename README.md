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

## Live Web Application (Instance Terminated)
**Demo Recording:** https://drive.google.com/file/d/1Gdskxt4ddbn_8LfSQvx2M50s666Y9zWp/view?usp=sharing
**URL (Terminated):** [Deployed Flask App](http://ec2-18-116-49-118.us-east-2.compute.amazonaws.com/)  

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

## Visual Studio Code Hierarchy

```bash
JAN25-P01/   # Project Root
│── data/
│   ├── cust-churn-data.ipynb  # Jupyter Notebook for EDA & Feature Engineering
│── model/
│   ├── rf1_model.pkl  # Final Model Export
│── src/
│   ├── app.py  # Flask API for Churn Prediction
│   ├── input_processing.py  # Preprocessing helper functions
│   ├── model.py  # Load Final Model
│   ├── test_api.py  # Test API functionality
│── static/
│   ├── css/
│   │   ├── styles.css  # Frontend styling
│── templates/
│   ├── home.html  # Homepage UI
│   ├── cust_churn_pred.html  # Customer input & results page
│── requirements.txt  # Dependencies for the project
│── README.md
│── Dockerfile  # Containerization setup
```

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



## AI300 Capstone Grading

### Feedback from Instructor Team

Hi Ruixin,

Your overall work—including UI/UX, user flow, extra features like the progress bar, and a well-organized README (thanks for the folder structure haha)—is amazing!

- Great job validating input fields in the form! Small details like this enhance user experience.

- When clicking the predict button, the page refreshes and jumps to the top. Using a modal to display results with navigation buttons (e.g., ""Try Again"" or ""Go Home"") would improve usability.

- Instead of hardcoding values like website = 'http://localhost:5000', consider storing them in a .env file. For larger projects with multiple endpoints, managing configurations in one place makes maintenance much easier.

- Each model has different preprocessing needs. For example, Logistic Regression may require feature scaling and one-hot encoding, while Catboost handles categorical variables internally and doesn’t need scaling. If you switch from Logistic Regression to Catboost, removing unnecessary preprocessing steps can improve efficiency.

- CatBoost handles missing values internally, so dropping rows may result in unnecessary data loss. It's better to let the model process them when possible.

- No need to manually apply one-hot encoding for CatBoost—it natively supports categorical features, making preprocessing more efficient.

Excellent work across the board! You’ve demonstrated strong skills in data preprocessing, model selection, and Flask deployment. Your documentation is thorough, and your Git practices are solid. Fantastic job—congrats on completing the AI300 course! 🚀


### Total Score: 20 / 20

Data Exploration: 6 / 6 marks
- [x] SQL used to successfully retrieve dataset from remote Heicoders database
- [x] SQL query should retrieve at least one column from each table:
churn_status, account, account_usage, customer and city tables
- [x] At least 2 charts used to visualise columns in dataset (e.g. with matplotlib or plotly)
- [x] Evidence of data preprocessing and/or feature engineering
e.g. column data type conversions, handling missing values, one hot encoding, etc.

Model Selection: 5 / 5 marks
- [x] Experiment with at least 2 model algorithms (e.g. catboost, xgboost, lgbm)
- [x] Evidence of hyperparameter tuning (e.g. GridSearchCV, RandomizedSearchCV, etc)
- [x] Calculate offline AUC of selected model
- [x] Export selected final model to .pkl file using joblib library

Remote GitHub Repository: 4 / 4 marks
- [x] Evidence of multiple commits with meaningful commit messages
- [x] Contains latest code for research notebook & Flask web app
- [x] Contains required documentation specified in grading rubric

Flask Web Application: 5 / 5 marks
- [x] Implement Model() class that loads model from .pkl file and generate predictions
- [x] Web app should support functionality of generating binary predictions
- [x] Web app is hosted on a publicly accessible website
