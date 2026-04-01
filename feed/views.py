from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FeedPurchase, FeedUsage, FeedType
from .serializers import FeedPurchaseSerializer,FeedUsageSerializer,FeedTypeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from django.db.models import Sum
from django.db import transaction


class FeedTypeViewSet(ModelViewSet):
    queryset = FeedType.objects.all()
    serializer_class = FeedTypeSerializer

class FeedPurchaseViewSet(ModelViewSet):
    queryset = FeedPurchase.objects.all()
    serializer_class = FeedPurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FeedPurchase.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedUsageViewSet(ModelViewSet):
    queryset = FeedUsage.objects.all()
    serializer_class = FeedUsageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return FeedUsage.objects.filter(user=self.request.user)

    @transaction.atomic
    def perform_create(self, serializer):
        user = self.request.user
        quantity_needed = serializer.validated_data['quantity_used_kg']
        feed_type = serializer.validated_data['feed_type']
        pond = serializer.validated_data['pond']

        purchases = FeedPurchase.objects.filter(
            user=user,
            pond=pond,
            feed_type=feed_type,
            remaining_quantity__gt=0
        ).order_by('purchase_date')

        total_available = purchases.aggregate(
            total=Sum('remaining_quantity')
        )['total'] or 0

        if total_available < quantity_needed:
            raise serializers.ValidationError("Not enough feed available")

        for purchase in purchases:
            if quantity_needed <= 0:
                break

            if purchase.remaining_quantity >= quantity_needed:
                purchase.remaining_quantity -= quantity_needed
                purchase.save()
                quantity_needed = 0
            else:
                quantity_needed -= purchase.remaining_quantity
                purchase.remaining_quantity = 0
                purchase.save()

        serializer.save(user=user)
