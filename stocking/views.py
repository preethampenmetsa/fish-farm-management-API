from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Stocking
from .serializers import StockingSerializer

class StockingViewSet(ModelViewSet):
    serializer_class = StockingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Stocking.objects.filter(pond__user=self.request.user)