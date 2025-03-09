import re
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

def validate(input_dict):
    """
    Validates input data for the customer churn model.

    Args:
        input_dict (dict): Dictionary containing input data.

    Returns:
        list: A list of validation error messages (empty if no errors).
    """
    errors = []

    required_fields = [
        "tenure_months", "num_referrals", "total_monthly_fee", "area_id",
        "num_dependents", "contract_type_encoded", "age",
        "not_credit_card", "total_charges_quarter", "total_premium_services"
    ]

    # 1️⃣ Check for Missing or Empty Fields
    for field in required_fields:
        if field not in input_dict or str(input_dict[field]).strip() == "":
            errors.append(f"Missing or empty field: {field}")

    # 2️⃣ Validate Numeric Fields
    try:
        if "tenure_months" in input_dict:
            tenure = float(input_dict["tenure_months"])
            if tenure < 0:
                errors.append("tenure_months must be >= 0.")

        if "num_referrals" in input_dict:
            num_referrals = int(input_dict["num_referrals"])
            if num_referrals < 0:
                errors.append("num_referrals must be >= 0.")

        if "total_monthly_fee" in input_dict:
            total_fee = float(input_dict["total_monthly_fee"])
            if total_fee < 0:
                errors.append("total_monthly_fee must be >= 0.")

        if "num_dependents" in input_dict:
            num_dependents = int(input_dict["num_dependents"])
            if num_dependents < 0 or num_dependents > 10:
                errors.append("num_dependents must be between 0 and 10.")

        if "contract_type_encoded" in input_dict:
            contract_type = int(input_dict["contract_type_encoded"])
            if contract_type not in [0, 1, 2]:  # Adjust based on valid contract types
                errors.append("contract_type_encoded must be 0, 1, or 2.")

        if "age" in input_dict:
            age = int(input_dict["age"])
            if age < 10 or age > 120:
                errors.append("age must be between 10 and 120.")

        if "not_credit_card" in input_dict:
            not_credit_card = int(input_dict["not_credit_card"])
            if not_credit_card not in [0, 1]:
                errors.append("not_credit_card must be 0 or 1.")

        if "total_charges_quarter" in input_dict:
            total_charges = float(input_dict["total_charges_quarter"])
            if total_charges < 0:
                errors.append("total_charges_quarter must be >= 0.")

        if "total_premium_services" in input_dict:
            premium_services = int(input_dict["total_premium_services"])
            if premium_services < 0:
                errors.append("total_premium_services must be >= 0.")

    except ValueError as e:
        errors.append(f"Invalid numeric value: {e}")

    # 3️⃣ Validate Area ID (if it has a specific format)
    if "area_id" in input_dict:
        area_id = input_dict["area_id"].strip()
        if not re.match(r"^[A-Za-z0-9]+$", area_id):  # Example format: Alphanumeric
            errors.append("area_id must be alphanumeric.")

    return errors
