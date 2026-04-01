from rest_framework import serializers
from .models import Mortality


class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortality
        fields = "__all__"
        read_only_fields = ["id"]