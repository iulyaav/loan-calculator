from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.service.service import compute_loan_parameters


class LoanRequestSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    monthly_rate = serializers.FloatField(required=False)
    payments = serializers.IntegerField(required=False)


class LoanCalculatorView(APIView):
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

        serializer = LoanRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = compute_loan_parameters(**serializer.data)

        return Response(result)
