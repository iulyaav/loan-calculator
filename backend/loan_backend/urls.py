from django.contrib import admin
from django.urls import path

from loan_backend.views.loan_calculator import LoanCalculatorView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoanCalculatorView.as_view(), name="loan_calculator"),
]
