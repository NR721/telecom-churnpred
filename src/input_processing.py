import numpy as np

def format_model_inputs(input_dict):
    """
    Extracts and formats input parameters for the machine learning model.

    Args:
        input_dict (dict): Dictionary containing input data.

    Returns:
        np.ndarray: A 2D NumPy array with formatted inputs.
    """
    try:
        # Convert input values
        tenure_months = float(input_dict['tenure_months'])
        num_referrals = int(input_dict['num_referrals'])
        total_monthly_fee = float(input_dict['total_monthly_fee'])
        area_id = str(input_dict['area_id']).strip()  # Keep it as a string
        num_dependents = int(input_dict['num_dependents'])
        contract_type_encoded = int(input_dict['contract_type_encoded'])
        age = int(input_dict['age'])
        not_credit_card = int(input_dict['not_credit_card'])
        total_charges_quarter = float(input_dict['total_charges_quarter'])
        total_premium_services = int(input_dict['total_premium_services'])

        # Prepare input for the model (ensure it's a 2D array)
        parameters = np.array([[
            tenure_months, num_referrals, total_monthly_fee, area_id, 
            num_dependents, contract_type_encoded, age, not_credit_card, 
            total_charges_quarter, total_premium_services
        ]], dtype=object)  # Use dtype=object to allow strings

        return parameters
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}")
    except ValueError as e:
        raise ValueError(f"Invalid data format: {e}")
