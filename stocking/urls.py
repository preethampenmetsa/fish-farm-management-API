from rest_framework.routers import DefaultRouter
from .views import StockingViewSet

router = DefaultRouter()
router.register(r'stockings', StockingViewSet, basename='stocking')

urlpatterns = router.urls