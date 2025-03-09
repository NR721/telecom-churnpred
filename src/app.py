from flask import Flask, request, render_template, jsonify, send_file
import joblib
from input_processing import format_model_inputs

app = Flask(__name__)

# 1: Response with Text
@app.route('/')  # default method=['GET']
def home_page():
    return render_template('home.html')  # Renders the styled home page

# 2: Respond with HTML template
@app.route('/cust_churn_pred', methods=['GET', 'POST'])
def get_html():
    if request.method == 'POST':
        # Load the model
        model = joblib.load('model/rf1_model.pkl')
        
       # Extract inputs from form
        input_data = request.form.to_dict()

        try:
            # Format input data
            parameters = format_model_inputs(input_data)

            # Make a binary prediction (outputs 1 or 0)
            prediction = model.predict(parameters)

            # Convert prediction result to readable text
            prediction_text = "Likely to Churn" if prediction == 1 else "Retained"

            return render_template('cust_churn_pred.html', prediction=prediction_text)
        
        except Exception as e:
            return render_template('cust_churn_pred.html', prediction=f"Error: {e}")
        
    # If it's a GET request, just render the form
    return render_template('cust_churn_pred.html')

# 3: Response with JSON
@app.route('/api_json', methods=['POST'])
def get_json():
    try:
        request_data = request.get_json()
        # Validate JSON input
        required_fields = [
            "tenure_months", "num_referrals", "total_monthly_fee", "area_id",
            "num_dependents", "contract_type_encoded", "age",
            "not_credit_card", "total_charges_quarter", "total_premium_services"
        ]
        for field in required_fields:
            if field not in request_data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        # Load the model
        model = joblib.load('model/rf1_model.pkl')

       # Format input data
        parameters = format_model_inputs(data)

        # Make a binary prediction (outputs 1 or 0)
        prediction = model.predict(parameters)[0]

        # Convert prediction result to readable text
        prediction_text = "Likely to Churn" if prediction == 1 else "Retained"

        return jsonify({
            "success": True,
            "prediction": prediction_text
        })

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
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