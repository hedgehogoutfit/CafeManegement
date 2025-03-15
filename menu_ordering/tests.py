from django.test import TestCase, Client
from .models import Menu, Order
from django.urls import reverse

# class TestModels(TestCase):
#     def setUp(self):
#         self.order = Order.objects.create(
#
#         )


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.orders_url = reverse('all_orders')
        self.create_order_url = reverse('create_order')
        Menu.objects.create(dish_id=1, dish_name='test_banana', price=5.00)
        Menu.objects.create(dish_id=2, dish_name='test_apple', price=3.00)
        Menu.objects.create(dish_id=5, dish_name='test_corn', price=4.00)


    def test_create_order(self):
        response = self.client.post(self.create_order_url, {
            'table_number': 1,
            'menu_item': ['1,2', '2,2', '5,1']
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.last().total_price, 20.00)


    def test_all_orders(self):
        response = self.client.get(self.orders_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/all_orders.html')