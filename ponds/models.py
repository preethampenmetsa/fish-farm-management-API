from django.db import models
from django.contrib.auth import get_user_model

class Pond(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ponds')

    name = models.CharField(max_length=100)
    area_acres = models.FloatField()

    lease_cost_per_acre_per_year = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    lease_start_date = models.DateField(null=True, blank=True)
    lease_end_date = models.DateField(null=True, blank=True)
