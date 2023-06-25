from order.views import order
from django.urls import path

urlpatterns = [
    path('', order, name='order'),
    path('<int:item_id>/', order, name='order_add')
]
