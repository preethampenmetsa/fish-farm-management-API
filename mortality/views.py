from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Mortality
from .serializers import MortalitySerializer


class MortalityViewSet(ModelViewSet):
    serializer_class = MortalitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Mortality.objects.filter(
            stocking__pond__user=self.request.user
        )