from django.db import models
from ponds.models import Pond
from django.contrib.auth import get_user_model


class FeedType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class FeedPurchase(models.Model):

    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE)

    quantity_kg = models.FloatField()
    price_per_kg = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()
    remaining_quantity = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.remaining_quantity = self.quantity_kg
        super().save(*args, **kwargs)

class FeedUsage(models.Model):

    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE)
    feed_type = models.CharField(max_length=100)
    quantity_used_kg = models.FloatField()
    date = models.DateField()