import numpy_financial as npf
from django.conf import settings


def compute_monthly_repaiment(amount=None, monthly_rate=None, payments=None):
    if monthly_rate is None and payments is None:
        raise Exception()

    loan = {
        "amount": amount,
        "monthly_rate": monthly_rate,
        "payments": payments
    }
    
    if monthly_rate and payments:
        check_interest()
    elif monthly_rate:
        loan["payments"] = get_number_of_payments(amount, monthly_rate)
    else:
        loan["monthly_rate"] = abs(get_monthly_rate(amount, payments))

    return loan


def get_monthly_rate(amount, payments, interest=settings.INTEREST_RATE):
    """Get rate to pay the loan in a given number of months.
    """
    return round(npf.pmt(interest/12, payments, amount), 2)

def get_number_of_payments(amount, monthly_rate, interest=settings.INTEREST_RATE):
    """Get the number of months of the loan."""

    return npf.nper(interest/12, -monthly_rate, amount)

