from rest_framework.routers import DefaultRouter
from .views import PondViewSet

router = DefaultRouter()
router.register(r'ponds', PondViewSet, basename='pond')

urlpatterns = router.urls