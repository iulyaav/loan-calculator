from django.db import models

class Loan(models.Model):
    amount = models.DecimalField(decimal_places=2)
    payments_number = models.IntegerField()

    class Meta:
        proxy = True