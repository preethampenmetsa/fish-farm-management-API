from rest_framework import serializers
from .models import FeedPurchase, FeedUsage, FeedType


class FeedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedType
        fields = '__all__'

class FeedPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedPurchase
        fields = '__all__'
        read_only_fields = ['user', 'remaining_quantity']


class FeedUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedUsage
        fields = '__all__'
        read_only_fields = ['user']