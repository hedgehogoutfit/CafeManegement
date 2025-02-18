from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:order_id>", views.order_detail, name="detail"),
    path('menu/', views.place_order, name="menu"),
    path('create/<str:menu_ids>/', views.create_order, name='create_order'),
    path('<int:order_id>/delete', views.delete_order, name='delete_order'),
]