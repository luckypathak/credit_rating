import json
import pandas as pd

def calc_ltv(loan_amount, property_value):
    return loan_amount / property_value if property_value != 0 else 0

def calc_dti(debt_amount, annual_income):
    return debt_amount / annual_income if annual_income != 0 else 0

def calc_risk_score(mortgage):
    risk_score = 0
    
    # Loan-to-Value (LTV) Ratio
    ltv = calc_ltv(mortgage["loan_amount"], mortgage["property_value"])
    if ltv > 0.9:
        risk_score += 2
    elif ltv > 0.8:
        risk_score += 1
    
    # Debt-to-Income (DTI) Ratio
    dti = calc_dti(mortgage["debt_amount"], mortgage["annual_income"])
    if dti > 0.5:
        risk_score += 2
    elif dti > 0.4:
        risk_score += 1
    
    # Credit Score
    credit_score = mortgage["credit_score"]
    if credit_score >= 700:
        risk_score -= 1
    elif credit_score < 650:
        risk_score += 1
    
    # Loan Type
    if mortgage["loan_type"] == "fixed":
        risk_score -= 1
    elif mortgage["loan_type"] == "adjustable":
        risk_score += 1
    
    # Property Type
    if mortgage["property_type"] == "condo":
        risk_score += 1
    
    return risk_score

def calc_credit_rating(mortgages):
    total_risk_score = 0
    total_credit_score = 0
    num_mortgages = len(mortgages)
    
    for mortgage in mortgages:
        total_risk_score += calc_risk_score(mortgage)
        total_credit_score += mortgage["credit_score"]
    
    avg_credit_score = total_credit_score / num_mortgages
    
    # Risk score on avg credit score
    if avg_credit_score >= 700:
        total_risk_score -= 1
    elif avg_credit_score < 650:
        total_risk_score += 1
    
    # Final credit rating
    if total_risk_score <= 2:
        return "AAA"
    elif 3 <= total_risk_score <= 5:
        return "BBB"
    else:
        return "C"

def get_file_data(file_path):
    # for json file
    if file_path.endswith(".json"):
        with open(file_path, "r") as f:
            return json.load(f).get("mortgages", [])
    # for csv file
    elif file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    # for xlsx file
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use JSON, CSV, or XLSX.")
    
    # mandatory colm's for the application
    required_columns = {"credit_score", "loan_amount", "property_value", "annual_income", "debt_amount", "loan_type", "property_type"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"Missing required columns in file: {required_columns - set(df.columns)}")
    
    return df.to_dict(orient="records")

def get_json_data():
    # complete json data
    try:
        data = json.loads(input("Enter JSON data: ").strip())
        return data.get("mortgages", [])
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format. Please check your input.")

def get_manual_data():
    # for manual data entries
    return [
        {
            "credit_score": int(input("Credit Score: ")),
            "loan_amount": float(input("Loan Amount: ")),
            "property_value": float(input("Property Value: ")),
            "annual_income": float(input("Annual Income: ")),
            "debt_amount": float(input("Debt Amount: ")),
            "loan_type": input("Loan Type (fixed/adjustable): ").strip().lower(),
            "property_type": input("Property Type (single_family/condo): ").strip().lower()
        }
        for _ in range(int(input("Enter number of mortgages: ")))
    ]

def load_data():
    # input methods
    choices = {"1": get_file_data, "2": get_json_data, "3": get_manual_data}
    choice = input("Choose input method:\n1. Load from a file (JSON, CSV, XLSX)\n2. Enter JSON data manually\n3. Enter data one by one\nEnter choice (1/2/3): ").strip()
    
    if choice not in choices:
        raise ValueError("Invalid choice. Please enter 1, 2, or 3.")
    
    # Call chosen function with file path if needed
    return choices[choice](input("Enter file path: ").strip()) if choice == "1" else choices[choice]()

if __name__ == "__main__":
    mortgages = load_data()
    print("Credit Rating:", calc_credit_rating(mortgages))
