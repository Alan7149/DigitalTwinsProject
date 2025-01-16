from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    availability = models.BooleanField()
    stock_levels = models.IntegerField()
    lead_time = models.IntegerField()  # Days
    manufacturing_lead_time = models.IntegerField()  # Days
    defect_rate = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    revenue_generated = models.FloatField()
    customer_demographics = models.JSONField()
    shipping_time = models.IntegerField()  # Days
    shipping_cost = models.FloatField()
    transportation_mode = models.CharField(max_length=100)
    route = models.CharField(max_length=255)
    cost = models.FloatField()  # Total cost for the order

    def __str__(self):
        return f"Order for {self.product.name}"


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    production_volume = models.IntegerField()
    manufacturing_cost = models.FloatField()
    inspection_results = models.JSONField()

    def __str__(self):
        return self.name