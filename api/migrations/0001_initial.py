# Generated by Django 5.1.5 on 2025-01-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_type', models.CharField(max_length=255)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('price', models.FloatField()),
                ('stock_levels', models.IntegerField()),
                ('lead_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Logistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route', models.CharField(max_length=255)),
                ('transportation_mode', models.CharField(max_length=100)),
                ('shipping_cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_quantity', models.IntegerField()),
                ('revenue_generated', models.FloatField()),
                ('customer_demographics', models.JSONField()),
            ],
        ),
    ]