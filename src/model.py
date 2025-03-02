import joblib
import numpy as np

class Model:
    def __init__(self):
        self.model = joblib.load('model/rf1_model.pkl')
     
    def predict(self, input_features):
        input_features = np.array(input_features)  # Ensure it's a NumPy array
        input_features = input_features.reshape(1, -1)  # Convert to 2D
        return self.model.predict(input_features)

# # Test example to ensure model works
# cust_churn_data_example = {
#     "tenure_months": 3,
#     "num_referrals": 3,
#     "total_monthly_fee": 83.90,
#     "area_id": "607",
#     "num_dependents": 0,
#     "contract_type_encoded":2,
#     "age": 75,
#     "not_credit_card": 0,
#     "total_charges_quarter": 267.40,
#     "total_premium_services": 1
# }
# model_inputs = list(cust_churn_data_example.values())

# print(model_inputs)                  # [3, 3, 83.90, "607", 0, 2, 75, 0, 267.4, 1]
# print(Model().predict(model_inputs)) #  1 = will churn