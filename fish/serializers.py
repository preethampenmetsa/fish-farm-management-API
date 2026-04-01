from rest_framework import serializers
from .models import FishType

class FishTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FishType
        fields = '__all__'