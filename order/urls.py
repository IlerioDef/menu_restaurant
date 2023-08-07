from order.views import order
from django.urls import path

urlpatterns = [
    path('', order, name='order'),
    path("<int:item_id>/<str:action>/", order, name='order_add'),
]
