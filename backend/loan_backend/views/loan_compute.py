from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from loan_backend.service.exceptions import ValidationError
from loan_backend.service.service import compute_monthly_repaiment


class LoanCompute(APIView):
    def get(self, request, format=None):
        """
        Return a loan result based on parameters:
        1. if amount + number of payments => monthly rate
        2. if amount + monthly rate => number of payments
        3. if amount + number of payments + monthly rate => check interest rate

        Because all these parameters are coming from the same
        user input, we will reuse the same endpoint and split it further
        in the service module.
        """

        amount = request.query_params.get("amount", None)
        monthly_rate = request.query_params.get("monthly", None)
        payments = request.query_params.get("payments", None)

        if amount is None or amount == 0:
            raise ValidationError("Amount is missing")

        result = compute_monthly_repaiment(amount, monthly_rate, payments)

        return Response(result)
