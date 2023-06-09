from django.contrib import admin

from core.models import Item, Allergen, Category

admin.site.register(Item)
admin.site.register(Allergen)
admin.site.register(Category)

