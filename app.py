#app.py
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Load the model
        model = joblib.load('catboost_model.pkl')

        gender = request.form['gender']
        married = request.form['married']
        dependents = int(request.form['dependents'])
        education = request.form['education']
        self_employed = request.form['self_employed']
        applicant_income = float(request.form['applicant_income'])
        coapplicant_income = float(request.form['coapplicant_income'])
        loan_amount = float(request.form['loan_amount'])
        loan_amount_term = float(request.form['loan_amount_term'])
        credit_history = float(request.form['credit_history'])
        property_area = request.form['property_area']
        total_income = applicant_income + coapplicant_income
        loan_amt_income_ratio = float(loan_amount) / float(total_income)

        # Get the parameters for the prediction
        parameters = [gender, married, dependents, education, self_employed, applicant_income, coapplicant_income, loan_amount, loan_amount_term, credit_history, property_area, total_income, loan_amt_income_ratio]

        # Make a binary prediction (outputs 1 or 0)
        prediction = model.predict(parameters)

        # Return the result along with the form
        return render_template('home.html', prediction=prediction)

    # If it's a GET request, just render the form
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)