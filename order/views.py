from django.http import HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect

from core.models import Item
from .order import Order


def order(request, item_id=None, action="increase"):
    menu_order = Order(request)

    if item_id is not None and action == 'increase':
        menu_order.add(product_id=item_id, quantity=1)
        menu_order.save()
    elif action == 'decrease':
        menu_order.add(product_id=item_id, quantity=-1)
        menu_order.save()
    item = Item.objects.all()
    context = {
        'menu_order': menu_order,
        'item': item,
    }
    if request.GET.get('next'):
        return redirect(request.GET.get('next'))


    return render(request, 'order.html', context)

