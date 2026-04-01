from django.db import models
from stocking.models import Stocking

class MortalityReason(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Mortality(models.Model):
    stocking = models.ForeignKey(
        Stocking,
        on_delete=models.CASCADE,
        related_name="mortalities"
    )

    date = models.DateField()
    dead_count = models.PositiveIntegerField()

    reason = models.ForeignKey(
        MortalityReason,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def clean(self):
        # Cannot record mortality for inactive stocking
        if not self.stocking.is_active:
            raise ValueError("Cannot add mortality to inactive stocking")

        # Dead count must be positive
        if self.dead_count <= 0:
            raise ValueError("Dead count must be greater than zero")

        # Optional (important): prevent over-death
        total_dead = sum(m.dead_count for m in self.stocking.mortalities.all())
        if total_dead + self.dead_count > self.stocking.fish_count:
            raise ValueError("Total mortality exceeds stocked fish count")

    def save(self, *args, **kwargs):
        self.full_clean()  # ensures clean() is called
        super().save(*args, **kwargs)

