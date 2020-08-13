from django.test import TestCase

from backend.service import service, exceptions

class ServiceTestCase(TestCase):

    def test_compute_loan_parameters__validation_error(self):
        with self.assertRaises(exceptions.ValidationError):
            service.compute_loan_parameters(1000, None, None)
    
    def test_compute_loan_parameters__update_monthly_rate(self):
        default_loan = {
            "amount": 1000,
            "monthly_rate": None,
            "payments": 10
        }
        result = service.compute_loan_parameters(**default_loan)
        self.assertIsNot(result["monthly_rate"], None)
        self.assertEqual(result["amount"], default_loan["amount"])
        self.assertEqual(result["payments"], default_loan["payments"])
        self.assertIn("interest", result)


    def test_compute_loan_parameters__with_interest_message(self):
        default_loan = {
            "amount": 1000,
            "monthly_rate": 15.5,
            "payments": 10
        }
        result = service.compute_loan_parameters(**default_loan)
        self.assertIs(result["monthly_rate"], default_loan["monthly_rate"])
        self.assertEqual(result["amount"], default_loan["amount"])
        self.assertEqual(result["payments"], default_loan["payments"])
        self.assertIn("interest", result)
        self.assertIn("interest_msg", result)

    def test_compute_loan_parameters__update_payments(self):
        default_loan = {
            "amount": 1000,
            "monthly_rate": 15.5,
            "payments": None
        }
        result = service.compute_loan_parameters(**default_loan)
        self.assertEqual(result["monthly_rate"], default_loan["monthly_rate"])
        self.assertEqual(result["amount"], default_loan["amount"])
        self.assertIsNot(result["payments"], None)
        self.assertIn("interest", result)