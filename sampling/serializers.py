from rest_framework import serializers
from .models import Sampling


class SamplingSerializer(serializers.ModelSerializer):
    total_fish = serializers.ReadOnlyField()
    average_weight = serializers.ReadOnlyField()

    class Meta:
        model = Sampling
        fields = "__all__"

    def validate(self, data):
        # Example API-level validation
        if data.get("sample_date") is None:
            raise serializers.ValidationError("Sample date is required")

        return data