from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from .models import Menu, Order, OrdersMenu
from typing import List

def all_orders(request):

    orders = Order.objects.all()
    return render(request, 'orders/all_orders.html', {'orders': orders})

def order_detail(request, order_id):
    order = Order.objects.get(order_id=order_id)
    order_items = order.ordersmenu_set.all()

    return render(request, 'orders/order_detail.html', {
        'order': order,
        'order_items': order_items
    })

def place_order(request):
    """Choose items from menu"""

    if request.method == "POST":
        menu_ids = request.POST.getlist('dish_ids')

        # Use `reverse` to construct the URL for 'create_order' and pass the arguments
        return redirect(reverse('create_order', kwargs={'menu_ids': ','.join(menu_ids)}))
    menu_items = Menu.objects.all()
    return render(request, 'orders/menu.html', {'menu_items': menu_items})

def create_order(request, menu_ids: str):
    menu_ids_list = menu_ids.split(',')
    objects = Menu.objects.filter(dish_id__in=menu_ids_list)

    if request.method == "POST":
        data= request.POST.dict()
        table_number = data.pop('table_number')
        order = Order.objects.create(table_number=int(table_number))
        for dish_id, quantity in data.items():
            try:
                OrdersMenu.objects.create(order=order, dish_id=dish_id, quantity=quantity)
            except ValueError:
                pass
        order.save()
        # todo flash massage
        return redirect("detail", order_id=order.order_id)
    return render(request, 'orders/create_order.html', {'objects': objects})

def delete_order(request, order_id):
    Order.objects.filter(order_id=order_id).delete()
    return HttpResponse("Delete an order!")



def change_status(request, order_id):
    """Пользователь через интерфейс выбирает заказ по ID и изменяет его статус (“в ожидании”, “готово”, “оплачено”).
"""
    return HttpResponse("Change status for an order!")