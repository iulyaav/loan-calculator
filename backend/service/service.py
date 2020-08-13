import numpy_financial as npf
from django.conf import settings

from backend.service.exceptions import ValidationError

INTEREST_RATE_PER_MONTH = settings.INTEREST_RATE / 12

def compute_loan_parameters(amount=None, monthly_rate=None, payments=None):
    """Compute loan parameters using given values.
    
    1. if we have the amount + monthly rate + number of payments => interest
    2. if we have the amount + monthly rate => number of payments
    3. if we have the amount + number of payments => monthly rate

    We compute 2) and 3) using our pre-configured interest rate.
    However, when we check for an interest, the result will be compared
    with the pre-configured value and an appropriate message will be attached to the result.
    """
    
    if monthly_rate is None and payments is None:
        raise ValidationError

    loan = {
        "amount": amount,
        "monthly_rate": monthly_rate,
        "payments": payments,
        "interest": INTEREST_RATE_PER_MONTH,
    }

    if monthly_rate and payments:
        interest = get_interest(amount, monthly_rate, payments)
        loan["interest"] = interest
        if interest > INTEREST_RATE_PER_MONTH:
            loan["interest_msg"] = "The interest is above our threshold"
        elif interest < INTEREST_RATE_PER_MONTH:
            loan["interest_msg"] = "The interest is below our threshold"
    elif monthly_rate:
        loan["payments"] = get_number_of_payments(amount, monthly_rate)
    else:
        loan["monthly_rate"] = abs(get_monthly_rate(amount, payments))

    return loan


def get_monthly_rate(amount, payments):
    """Get rate to pay the loan in a given number of months
    """
    return round(npf.pmt(INTEREST_RATE_PER_MONTH, payments, amount), 2)

def get_number_of_payments(amount, monthly_rate):
    """Get the number of months of the loan."""
    return npf.nper(INTEREST_RATE_PER_MONTH, -monthly_rate, amount)

def get_interest(amount, monthly_rate, payments):
    """Return the interest rate.
    
    This operation needs the monthly rate to be negative,
    so we're doing multiplying a positive monthly rate by -1
    to support users sending us a positive value.

    The result comes back as negative number and it is 
    rounded to make it easier for the user to read - 
    i.e. if the result is -2.0184122884653117, then the rate is
    2.01 per period.
    """
    if monthly_rate > 0:
        monthly_rate *= -1
    return abs(round(npf.rate(payments, monthly_rate, amount, 0), 2))
