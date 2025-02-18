# Generated by Django 5.1.5 on 2025-01-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_ordering', '0002_order_dishes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
