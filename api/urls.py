from rest_framework.routers import DefaultRouter
from .views import InventoryViewSet, OrdersViewSet, LogisticsViewSet

router = DefaultRouter()
router.register(r'inventory', InventoryViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'logistics', LogisticsViewSet)

urlpatterns = router.urls
