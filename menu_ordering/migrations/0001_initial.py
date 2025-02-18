# Generated by Django 5.1.5 on 2025-01-26 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False)),
                ('dish_name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_number', models.IntegerField()),
                ('status', models.TextField(choices=[('в ожидании', 'Waiting'), ('готово', 'Ready'), ('оплачено', 'Paid')], default='в ожидании')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdersMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_ordering.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu_ordering.order')),
            ],
        ),
    ]
