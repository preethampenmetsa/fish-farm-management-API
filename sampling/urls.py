from rest_framework.routers import DefaultRouter
from .views import SamplingViewSet

router = DefaultRouter()
router.register(r'samplings', SamplingViewSet, basename="sampling")

urlpatterns = router.urls