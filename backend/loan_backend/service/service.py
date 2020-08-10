import numpy_financial as npf
from django.conf import settings

from loan_backend.service.exceptions import ValidationError

def compute_monthly_repaiment(amount=None, monthly_rate=None, payments=None):
    if monthly_rate is None and payments is None:
        raise ValidationError

    loan = {
        "amount": amount,
        "monthly_rate": monthly_rate,
        "payments": payments,
    }

    if monthly_rate and payments:
        interest = check_interest(amount, monthly_rate, payments)
        loan["interest"] = interest
        if interest > settings.INTEREST_RATE:
            loan["interest_msg"] = "The interest is above our threshold"
        elif interest < settings.INTEREST_RATE:
            loan["interest_msg"] = "The interest is below our threshold"
    elif monthly_rate:
        loan["payments"] = get_number_of_payments(amount, monthly_rate)
    else:
        loan["monthly_rate"] = abs(get_monthly_rate(amount, payments))

    return loan


def get_monthly_rate(amount, payments):
    """Get rate to pay the loan in a given number of months.
    """
    rate = get_rate()
    return round(npf.pmt(rate, payments, amount), 2)

def get_number_of_payments(amount, monthly_rate):
    """Get the number of months of the loan."""
    rate = get_rate()
    return npf.nper(rate, -monthly_rate, amount)

def get_rate(interest=settings.INTEREST_RATE):
    return interest / 12


def check_interest(amount, monthly_rate, payments):
    if monthly_rate > 0:
        monthly_rate *= -1
    return abs(round(npf.rate(payments, monthly_rate, amount, 0) * 12, 2))
