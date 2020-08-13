from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from backend.views.loan_calculator import LoanCalculatorView

class LoanCalculatorViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_view__200(self):
        request = self.factory.get('', {'amount': '100', 'payments': '5'})
        request.user = AnonymousUser()
        response = LoanCalculatorView.as_view()(request)
        self.assertEqual(response.status_code, 200) 

    def test_view__no_parameters(self):
        request = self.factory.get('')
        request.user = AnonymousUser()
        response = LoanCalculatorView.as_view()(request)
        self.assertEqual(response.status_code, 400)
    
    def test_view__required_parameter(self):
        request = self.factory.get('',  {'payments': '5'})
        request.user = AnonymousUser()
        response = LoanCalculatorView.as_view()(request)
        self.assertEqual(response.status_code, 400) 
    
    def test_view__parameter_type_validator(self):
        request = self.factory.get('',  {'amount': 'test', 'payments': '5'})
        request.user = AnonymousUser()
        response = LoanCalculatorView.as_view()(request)
        self.assertEqual(response.status_code, 400)