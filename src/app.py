from flask import Flask, request, render_template, jsonify, send_file
import joblib
import numpy as np

app = Flask(__name__)

# 1: Response with Text
@app.route('/')  # default method=['GET']
def home_page():
    return 'Welcome to the home page!'

# 2: Respond with HTML template
@app.route('/cust_churn_pred', methods=['GET', 'POST'])
def get_html():
    if request.method == 'POST':
        # Load the model
        model = joblib.load('model/rf1_model.pkl')
        
        tenure_months = float(request.form['tenure_months'])
        num_referrals = int(request.form['num_referrals'])
        total_monthly_fee = float(request.form['total_monthly_fee'])
        area_id = str(request.form['area_id']).strip()  # Keep it as a string
        num_dependents = int(request.form['num_dependents'])
        contract_type_encoded = int(request.form['contract_type_encoded'])
        age = int(request.form['age'])
        not_credit_card = int(request.form['not_credit_card'])
        total_charges_quarter = float(request.form['total_charges_quarter'])
        total_premium_services = int(request.form['total_premium_services'])

        # Prepare input for the model (ensure it's a 2D array)
        parameters = np.array([[
            tenure_months, num_referrals, total_monthly_fee, area_id, 
            num_dependents, contract_type_encoded, age, not_credit_card, 
            total_charges_quarter, total_premium_services
        ]], dtype=object)  # Use dtype=object to allow strings

        # Make a binary prediction (outputs 1 or 0)
        prediction = model.predict(parameters)

        # Convert prediction result to readable text
        prediction_text = "Likely to Churn" if prediction == 1 else "Retained"
    
        # Return the result along with the form
        return render_template('cust_churn_pred.html', prediction=prediction_text)

    # If it's a GET request, just render the form
    return render_template('cust_churn_pred.html')

# 3: Response with JSON
@app.route('/json', methods=['POST'])
def get_json():
    try:
        data = request.get_json()
        # Validate JSON input
        required_fields = [
            "tenure_months", "num_referrals", "total_monthly_fee", "area_id",
            "num_dependents", "contract_type_encoded", "age",
            "not_credit_card", "total_charges_quarter", "total_premium_services"
        ]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Load the model
        model = joblib.load('model/rf1_model.pkl')

        # Convert input values
        tenure_months = float(data['tenure_months'])
        num_referrals = int(data['num_referrals'])
        total_monthly_fee = float(data['total_monthly_fee'])
        area_id = str(data['area_id']).strip()  # Keep it as a string
        num_dependents = int(data['num_dependents'])
        contract_type_encoded = int(data['contract_type_encoded'])
        age = int(data['age'])
        not_credit_card = int(data['not_credit_card'])
        total_charges_quarter = float(data['total_charges_quarter'])
        total_premium_services = int(data['total_premium_services'])

        # Prepare input for the model (ensure it's a 2D array)
        parameters = np.array([[
            tenure_months, num_referrals, total_monthly_fee, area_id, 
            num_dependents, contract_type_encoded, age, not_credit_card, 
            total_charges_quarter, total_premium_services
        ]], dtype=object)  # Use dtype=object to allow strings

        # Make a binary prediction (outputs 1 or 0)
        prediction = model.predict(parameters)[0]

        # Convert prediction result to readable text
        prediction_text = "Likely to Churn" if prediction == 1 else "Retained"

        return jsonify({
            "success": True,
            "prediction": prediction_text
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4: Response with File (Bonus)
@app.route('/file')
def get_file():
    file_path = '../model/rf1_model.pkl'
    return send_file(file_path, download_name='rf1_model.pkl',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)