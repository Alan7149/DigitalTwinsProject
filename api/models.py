from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    stock_levels = models.IntegerField()
    lead_time = models.IntegerField()  # Days

    def __str__(self):
        return self.name

class Orders(models.Model):
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    revenue_generated = models.FloatField()

    def __str__(self):
        return f"Order for {self.product.name}"

class Logistics(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    shipping_time = models.IntegerField()  # Days
    shipping_cost = models.FloatField()

    def __str__(self):
        return f"Logistics for {self.order.id}"