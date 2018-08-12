from django.urls import path
from . import views 

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('order/<slug:slug>/', views.order_food, name='order'),
    path('remove_order/<slug:slug>/', views.remove_food_order, name='remove_order'),  
    path('orders/all/<slug:slug>/', views.all_orders_view, name='all_orders')
]