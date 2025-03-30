# import unittest
# import json
# import pandas as pd
# import random
# from credit_rating import (
#     calc_ltv, calc_dti, calc_risk_score,
#     calc_credit_rating, get_file_data
# )

# class TestCreditRating(unittest.TestCase):
#     def setUp(self):
#         self.mortgages = [
#             {
#                 "credit_score": 750,
#                 "loan_amount": 200000,
#                 "property_value": 250000,
#                 "annual_income": 60000,
#                 "debt_amount": 20000,
#                 "loan_type": "fixed",
#                 "property_type": "single_family"
#             },
#             {
#                 "credit_score": 680,
#                 "loan_amount": 150000,
#                 "property_value": 175000,
#                 "annual_income": 45000,
#                 "debt_amount": 10000,
#                 "loan_type": "adjustable",
#                 "property_type": "condo"
#             }
#         ]
    
#     def test_calc_ltv(self):
#         self.assertEqual(calc_ltv(200000, 250000), 0.8)
#         self.assertEqual(calc_ltv(150000, 175000), 0.8571428571428571)
#         self.assertEqual(calc_ltv(100000, 0), 0)
    
#     def test_calc_dti(self):
#         self.assertEqual(calc_dti(20000, 60000), 0.3333333333333333)
#         self.assertEqual(calc_dti(10000, 45000), 0.2222222222222222)
#         self.assertEqual(calc_dti(5000, 0), 0)
    
#     def test_calc_risk_score(self):
#         self.assertEqual(calc_risk_score(self.mortgages[0]), -1)
#         self.assertEqual(calc_risk_score(self.mortgages[1]), 4)
    
#     def test_high_credit_score(self):
#         mortgages = [
#             {
#                 "credit_score": 750,
#                 "loan_amount": 200000,
#                 "property_value": 250000,
#                 "annual_income": 60000,
#                 "debt_amount": 20000,
#                 "loan_type": "fixed",
#                 "property_type": "single_family"
#             }
#         ]
#         self.assertEqual(calc_credit_rating(mortgages), "AAA")
    
#     def test_low_credit_score_high_ltv(self):
#         mortgages = [
#             {
#                 "credit_score": 620,
#                 "loan_amount": 180000,
#                 "property_value": 200000,
#                 "annual_income": 50000,
#                 "debt_amount": 25000,
#                 "loan_type": "adjustable",
#                 "property_type": "condo"
#             }
#         ]
#         self.assertEqual(calc_credit_rating(mortgages), "C")
    
#     def test_medium_risk(self):
#         mortgages = [
#             {
#                 "credit_score": 680,
#                 "loan_amount": 150000,
#                 "property_value": 175000,
#                 "annual_income": 45000,
#                 "debt_amount": 10000,
#                 "loan_type": "adjustable",
#                 "property_type": "condo"
#             }
#         ]
#         self.assertEqual(calc_credit_rating(mortgages), "BBB")
    
#     def test_mixed_mortgages(self):
#         mortgages = [
#             {
#                 "credit_score": 750,
#                 "loan_amount": 200000,
#                 "property_value": 250000,
#                 "annual_income": 60000,
#                 "debt_amount": 20000,
#                 "loan_type": "fixed",
#                 "property_type": "single_family"
#             },
#             {
#                 "credit_score": 680,
#                 "loan_amount": 150000,
#                 "property_value": 175000,
#                 "annual_income": 45000,
#                 "debt_amount": 10000,
#                 "loan_type": "adjustable",
#                 "property_type": "condo"
#             }
#         ]
#         self.assertEqual(calc_credit_rating(mortgages), "BBB")
    
#     def test_calc_credit_rating(self):
#         rating = calc_credit_rating(self.mortgages)
#         print(f"Final Credit Rating: {rating}")
#         self.assertEqual(rating, "BBB")
    
#     def test_get_file_data_json(self):
#         with open("sample.json", "w") as f:
#             json.dump({"mortgages": self.mortgages}, f)
        
#         data = get_file_data("sample.json")
#         self.assertEqual(len(data), 2)
#         self.assertEqual(data[0]["credit_score"], 750)
#         self.assertEqual(calc_credit_rating(data), "BBB")
    
#     def test_get_file_data_csv(self):        
#         data = get_file_data("/home/lucky/Lucky/New/credit_rating_system/sample.csv")
#         self.assertEqual(len(data), 2)
#         self.assertEqual(data[1]["loan_type"], "adjustable")
#         self.assertEqual(calc_credit_rating(data), "BBB")
    
#     def test_get_file_data_xlsx(self):
#         data = get_file_data("/home/lucky/Lucky/New/credit_rating_system/sample.xlsx")
#         self.assertEqual(len(data), 2)
#         self.assertEqual(data[1]["property_type"], "condo")
#         self.assertEqual(calc_credit_rating(data), "BBB")
    
#     def test_large_dataset(self):
#         large_mortgages = [
#             {
#                 "credit_score": random.randint(500, 850),
#                 "loan_amount": random.randint(50000, 500000),
#                 "property_value": random.randint(100000, 1000000),
#                 "annual_income": random.randint(30000, 200000),
#                 "debt_amount": random.randint(5000, 50000),
#                 "loan_type": random.choice(["fixed", "adjustable"]),
#                 "property_type": random.choice(["single_family", "condo", "multi_family"])
#             } for _ in range(120)
#         ]
#         df = pd.DataFrame(large_mortgages)
#         df.to_csv("large_sample.csv", index=False)
        
#         data = get_file_data("large_sample.csv")
#         self.assertEqual(len(data), 120)
#         rating = calc_credit_rating(data)
#         print(f"Final Credit Rating for Large Dataset: {rating}")
    
# if __name__ == "__main__":
#     unittest.main()


import unittest
from credit_rating import (
    calc_ltv, calc_dti, calc_risk_score,
    calc_credit_rating, get_file_data
)

class TestCreditRating(unittest.TestCase):
    def setUp(self):
        self.mortgages = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
    
    def test_calc_ltv(self):
        self.assertAlmostEqual(calc_ltv(200000, 250000), 0.8)
        self.assertAlmostEqual(calc_ltv(150000, 175000), 0.8571428571428571)
        self.assertEqual(calc_ltv(100000, 0), 0)
    
    def test_calc_dti(self):
        self.assertAlmostEqual(calc_dti(20000, 60000), 0.3333333333333333)
        self.assertAlmostEqual(calc_dti(10000, 45000), 0.2222222222222222)
        self.assertEqual(calc_dti(5000, 0), 0)
    
    def test_calc_risk_score(self):
        self.assertEqual(calc_risk_score(self.mortgages[0]), -2)
        self.assertEqual(calc_risk_score(self.mortgages[1]), 3)
    
    def test_credit_rating_high_score(self):
        self.assertEqual(calc_credit_rating([self.mortgages[0]]), "AAA")
    
    def test_credit_rating_low_score(self):
        low_score_mortgage = {
            "credit_score": 620,
            "loan_amount": 180000,
            "property_value": 200000,
            "annual_income": 50000,
            "debt_amount": 25000,
            "loan_type": "adjustable",
            "property_type": "condo"
        }
        self.assertEqual(calc_credit_rating([low_score_mortgage]), "C")
    
    def test_credit_rating_medium_risk(self):
        self.assertEqual(calc_credit_rating([self.mortgages[1]]), "BBB")
    
    def test_mixed_credit_rating(self):
        self.assertEqual(calc_credit_rating(self.mortgages), "AAA")
    
    def test_large_dataset(self):
        data = get_file_data("large_sample.csv")
        self.assertEqual(len(data), 120)
        rating = calc_credit_rating(data)
        print(f"Final Credit Rating for Large Dataset: {rating}")
    
    def test_get_file_data_json(self):
        data = get_file_data("sample.json")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["credit_score"], 710)
        self.assertEqual(calc_credit_rating(data), "BBB")
    
    def test_get_file_data_csv(self):        
        data = get_file_data("sample.csv")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[1]["loan_type"], "adjustable")
        self.assertEqual(calc_credit_rating(data), "AAA")
    
    def test_get_file_data_xlsx(self):
        data = get_file_data("sample.xlsx")
        self.assertEqual(len(data), 2)
        self.assertEqual(data[1]["property_type"], "condo")
        self.assertEqual(calc_credit_rating(data), "AAA")
    
if __name__ == "__main__":
    unittest.main()
