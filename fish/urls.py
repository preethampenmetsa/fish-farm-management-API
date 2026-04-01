from rest_framework.routers import DefaultRouter
from .views import FishTypeViewSet

router = DefaultRouter()
router.register(r'fishes', FishTypeViewSet)

urlpatterns = router.urls