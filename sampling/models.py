from django.db import models
from django.core.exceptions import ValidationError
from stocking.models import Stocking


class Sampling(models.Model):
    stocking = models.ForeignKey(
        Stocking,
        on_delete=models.CASCADE,
        related_name="samplings"
    )

    sample_date = models.DateField()

    number_of_samples = models.PositiveIntegerField()
    batch_size = models.PositiveIntegerField()

    total_weight_grams = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    # -----------------------------
    # Derived Properties (OOP)
    # -----------------------------
    @property
    def total_fish(self):
        return self.number_of_samples * self.batch_size

    @property
    def avg_weight_grams(self):
        if self.total_fish == 0:
            return None
        return self.total_weight_grams / self.total_fish

    # -----------------------------
    # Validation (Data Integrity)
    # -----------------------------
    def clean(self):
        if self.number_of_samples <= 0:
            raise ValidationError("Number of samples must be > 0")

        if self.batch_size <= 0:
            raise ValidationError("Batch size must be > 0")

        if self.total_weight_grams <= 0:
            raise ValidationError("Total weight must be > 0")

        # Important: sampling date >= stocking date
        if self.sample_date < self.stocking.stocking_date:
            raise ValidationError("Sampling date cannot be before stocking date")

        # Optional: prevent sampling on inactive stocking
        if not self.stocking.is_active:
            raise ValidationError("Cannot sample inactive stocking")

    def save(self, *args, **kwargs):
        self.full_clean()  # ensures validation always runs
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stocking} - {self.sample_date}"