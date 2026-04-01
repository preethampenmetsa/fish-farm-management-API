from rest_framework import serializers
from .models import Pond

class PondSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pond
        fields = '__all__'
        read_only_fields = ['user']