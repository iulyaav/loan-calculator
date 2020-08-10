from django.contrib import admin
from django.urls import path

from loan_backend.views.loan_calculator import LoanCalculator

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoanCalculator.as_view(), name="loan"),
]
