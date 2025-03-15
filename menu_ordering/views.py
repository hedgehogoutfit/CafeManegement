from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView, ListView
from datetime import date
from .models import Menu, Order, OrderItems


class OrderListView(ListView):
    model = Order
    template_name = 'orders/all_orders.html'
class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'

def raschet_za_smenu(request):
    sql_line = f"""select order_id from menu_ordering_order
    where date(created_at) = {date.today()};"""
    orders = Order.objects.raw(sql_line)
    total = 0
    for order in orders:
        total += order.total_price
    return HttpResponse(f"Total amount for the last 24 hours: {total}$")

def create_order(request):

    objects = Menu.objects.all()

    if request.method == "POST":
        table_number = request.POST.get('table_number')
        menu_items = request.POST.getlist('menu_item')
        order = Order.objects.create(table_number=int(table_number))
        for item in menu_items:
            dish_id, quantity = item.split(',')
            try:
                OrderItems.objects.create(order=order, dish_id=dish_id, quantity=quantity)
            except ValueError:
                pass
        order.save()
        return redirect(reverse('order_detail', kwargs={'pk': order.pk}))
    return render(request, 'orders/create_order.html', {'objects': objects})


def delete_order(request, order_id):
    Order.objects.filter(order_id=order_id).delete()
    return HttpResponse("Delete an order!")



def change_status(request, order_id):
    """Пользователь через интерфейс выбирает заказ по ID и изменяет его статус (“в ожидании”, “готово”, “оплачено”).
"""
    return HttpResponse("Change status for an order!")