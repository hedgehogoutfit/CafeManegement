from django.urls import path

from . import views

urlpatterns = [
    path("", views.OrderListView.as_view(), name="all_orders"),
    path("<int:pk>/", views.OrderDetailView.as_view(), name="order_detail"),
    path('create/', views.create_order, name='create_order'),
    path('<int:order_id>/delete', views.delete_order, name='delete_order'),
    path('count/', views.raschet_za_smenu, name='count'),
]