from rest_framework.routers import DefaultRouter
from .views import MortalityViewSet

router = DefaultRouter()
router.register("mortalities", MortalityViewSet, basename="mortality")

urlpatterns = router.urls