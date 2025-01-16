from django.core.management.base import BaseCommand
from api.models import Inventory, Orders, Logistics

class Command(BaseCommand):
    help = "Seed the database with initial data"

    def handle(self, *args, **kwargs):
        # Seed Inventory data
        Inventory.objects.create(product_type="Electronics", sku="SKU123", stock_levels=100, lead_time=5, price=1500.00)
        Inventory.objects.create(product_type="Fashion", sku="SKU456", stock_levels=200, lead_time=3, price=500.00)

        # Seed Orders data
        Orders.objects.create(order_quantity=10, revenue_generated=1500.00, customer_demographics={"age": 25, "location": "India"})
        Orders.objects.create(order_quantity=5, revenue_generated=700.00, customer_demographics={"age": 30, "location": "USA"})

        # Seed Logistics data
        Logistics.objects.create(route="Mumbai-Delhi", transportation_mode="Truck", shipping_cost=500.00)
        Logistics.objects.create(route="Chennai-Bangalore", transportation_mode="Air", shipping_cost=1000.00)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database!"))
