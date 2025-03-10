import requests

# Define API URL
website = 'http://localhost:5000' 
url = f'{website}/api_json'

# Input data
model_inputs = {
    "tenure_months": 3,
    "num_referrals": 3,
    "total_monthly_fee": 83.90,
    "area_id": "607",
    "num_dependents": 0,
    "contract_type_encoded": 2,
    "age": 75,
    "not_credit_card": 0,
    "total_charges_quarter": 267.40,
    "total_premium_services": 1
}

# Send API request with JSON header
headers = {"Content-Type": "application/json"}
response = requests.post(url, json=model_inputs, headers=headers)

# Print status and response content
print(f"Status Code: {response.status_code}")

try:
    print("Response JSON:", response.json())  # Print JSON response
except requests.exceptions.JSONDecodeError:
    print("Error: Response is not in JSON format. Raw response:", response.text)
