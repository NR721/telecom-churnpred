from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Respond with text
@app.route('/', methods=['GET', 'POST'])
def home():
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
        return render_template('home.html', prediction=prediction_text)

    # If it's a GET request, just render the form
    return render_template('home.html')

# # 2: Response with HTML template
# @app.route('/html')
# def get_html():
#     return render_template('index.html')

# # 3: Response with JSON
# @app.route('/json')
# def get_json():
#     return {'success': True}

# # 4: Response with File (Bonus)
# @app.route('/file')
# def get_file():
#     file_path = '../model/rf1_model.pkl'
#     return send_file(file_path, download_name='rf1_model.pkl',
#                      as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)