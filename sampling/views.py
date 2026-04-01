from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Sampling
from .serializers import SamplingSerializer

class SamplingViewSet(ModelViewSet):
    serializer_class = SamplingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Sampling.objects.filter(
            stocking__pond__user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save()
