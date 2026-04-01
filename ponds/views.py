from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Pond
from .serializers import PondSerializer

class PondViewSet(ModelViewSet):
    serializer_class = PondSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Pond.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)