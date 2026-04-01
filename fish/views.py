from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import FishType
from .serializers import FishTypeSerializer

class FishTypeViewSet(ModelViewSet):
    queryset = FishType.objects.all()
    serializer_class = FishTypeSerializer
