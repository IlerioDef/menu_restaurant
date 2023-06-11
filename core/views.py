from django.shortcuts import render

from core.models import Item, Allergen


# Create your views here.

def core(request):
    return render(request, "core/core.html")


def menu(request):
    item = Item.objects.all()
    allergen = "yes"
    context = {
        'menu': item,
    }
    print('а это контекст, который передается', context)
    return render(request, "core/menu.html", context)

