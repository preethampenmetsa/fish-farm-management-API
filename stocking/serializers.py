from rest_framework import serializers
from .models import Stocking

class StockingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stocking
        fields = '__all__'

    def validate(self, data):
        pond = data.get('pond')
        fish_type = data.get('fish_type')

        # Check if active stocking already exists
        if Stocking.objects.filter(
            pond=pond,
            fish_type=fish_type,
            is_active=True
        ).exists():
            raise serializers.ValidationError(
                "Active stocking already exists. Close it before adding new one."
            )

        return data