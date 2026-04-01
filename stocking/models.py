from django.db import models
from fish.models import FishType
from ponds.models import Pond

class Stocking(models.Model):
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE, related_name='stockings')
    fish_type = models.ForeignKey(FishType, on_delete=models.CASCADE)

    fish_count = models.PositiveIntegerField()
    initial_avg_weight_grams  = models.PositiveIntegerField()

    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    stocking_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def initial_biomass_kg(self):
        return (self.fish_count * self.initial_avg_weight_grams) / 1000
    
class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=['pond', 'fish_type'],
            condition=models.Q(is_active=True),
            name='unique_active_stocking_per_pond_fish'
        )
    ]