from django.shortcuts import render

from core.models import Item
from .order import Order


def order(request, item_id=None, action="increase"):
    menu_order = Order(request)
    if item_id is not None and action == 'increase':
        print(menu_order.__dict__)
        menu_order.add(product_id=item_id, quantity=1)
        menu_order.save()
        print("NOW THIS", menu_order.__dict__)
    elif action == 'decrease':
        print(menu_order.__dict__, "DECREASING")
        menu_order.add(product_id=item_id, quantity=-1)
        menu_order.save()
    item = Item.objects.all()
    context = {
        'menu_order': menu_order,
        'item': item,
    }

    return render(request, 'order.html', context)
