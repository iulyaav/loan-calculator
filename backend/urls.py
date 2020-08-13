from django.contrib import admin
from django.urls import path

from backend.views.index import index
from backend.views.loan_calculator import LoanCalculatorView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index, name='index'),
    path("loan/", LoanCalculatorView.as_view(), name="loan_calculator"),
]
