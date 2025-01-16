from rest_framework.viewsets import ModelViewSet
from .models import Inventory, Orders, Logistics
from .serializers import InventorySerializer, OrdersSerializer, LogisticsSerializer

class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer

class OrdersViewSet(ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class LogisticsViewSet(ModelViewSet):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
