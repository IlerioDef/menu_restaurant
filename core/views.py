from django.shortcuts import render

from core.models import Item, Allergen


# Create your views here.

def core(request):
    return render(request, "core/core.html")


def menu(request):
    item = Item.objects.all()
    allergen = Allergen.objects.all()
    dictionary = {}

    for i in item:
        internal_dictionary = {

                 "id": i.id,
                 'name': i.name,
                 'slug': i.slug,
                 'category': (i.category.id, i.category.name),
                 'price': i.price,
                 'allergen': [x.name for x in Allergen.objects.filter(item=i.id)],
                 'image': i.image,
                 'thumbnail': i.get_thumbnail(),
                 'food_energy': i.food_energy,
                 'description': i.description,

             }
        dictionary[i.id] = internal_dictionary



    context = {
        # 'id': item.id,
        'menu': dictionary,
        # 'category' : item.category,
    }
    print('а это контекст, который передается', context)
    return render(request, "core/menu.html", context)
