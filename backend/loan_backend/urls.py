from django.contrib import admin
from django.urls import path

from loan_backend.views.loan_compute import LoanCompute

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoanCompute.as_view(), name="loan"),
]
