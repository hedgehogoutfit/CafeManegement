from django.db import models


class Menu(models.Model):
    dish_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    dish_name = models.TextField()
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.dish_name

class Order(models.Model):
    class Status(models.TextChoices):
        WAITING = "в ожидании"
        READY = "готово"
        PAID = "оплачено"

    order_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    table_number = models.IntegerField()
    status = models.TextField(choices=Status.choices, default=Status.WAITING)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - Table {self.table_number} - Status: {self.status} - Total Price: {self.total_price}"

    def calculate_total_price(self):
        # Sum the prices of all dishes in this order
        total = sum(
            item.dish.price * item.quantity for item in self.ordersmenu_set.all()
        )
        return total

    def save(self, *args, **kwargs):
        # Only calculate total_price after the order is saved and has a primary key
        if self.pk:
            self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)



class OrdersMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Foreign key to Order
    dish = models.ForeignKey(Menu, on_delete=models.CASCADE)    # Foreign key to Menu
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Order {self.order.order_id} - {self.dish.dish_name} x {self.quantity}"
