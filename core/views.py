from django.shortcuts import render

from core.models import Item, Allergen


# Create your views here.

def core(request):
    return render(request, "core/core.html")


def menu(request):
    menu = Item.objects.all()
    allergens = Allergen.objects.all()
    context = {
        'menu': menu,
        'allergens': allergens,
    }

    return render(request, "core/menu.html", context)
