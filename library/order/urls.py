from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders_view, name='orders_view'),
    path('create_order/<int:book_id>/', views.create_order, name='create_order'),
    path('close_order/<int:order_id>/', views.close_order, name='close_order'),
]
