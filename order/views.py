from django.shortcuts import render

from .order import Order


def order(request, item_id=None):
    menu_order = Order(request)

    if item_id is not None:
        print(menu_order.__dict__)
        menu_order.add(product_id=item_id)
        menu_order.save()
        print("NOW THIS", menu_order.__dict__)

    context = {
        'menu_order': menu_order
    }

    return render(request, 'order.html', context)
