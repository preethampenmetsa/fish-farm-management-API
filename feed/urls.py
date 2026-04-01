from rest_framework.routers import DefaultRouter
from .views import FeedPurchaseViewSet,FeedUsageViewSet, FeedTypeViewSet

router = DefaultRouter()
router.register('feed-types', FeedTypeViewSet)
router.register('feed-purchases', FeedPurchaseViewSet)
router.register('feed-usage', FeedUsageViewSet)

urlpatterns = router.urls