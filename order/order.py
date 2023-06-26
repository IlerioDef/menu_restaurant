from django.conf import settings

from core.models import Item


class Order(object):
    def __init__(self, request):
        self.session = request.session
        menu_order = self.session.get(settings.ORDER_SESSION_ID)

        if not menu_order:
            menu_order = self.session[settings.ORDER_SESSION_ID] = {}

        self.menu_order = menu_order

    # def __iter__(self):
    # for p, item in self.menu_order.items():
    #     self.menu_order[str(p)]["menu_order"] = Item.objects.get(pk=p)['id']
    #
    #     item['total_price'] = int(item['menu_order'].price * item['quantity']) / 100
    #
    #     yield item

    def __getitem__(self, request):
        return self.menu_order[request]

    def __setitem__(self, request, value):
        self.menu_order[request] = value

    def save(self):
        self.session[settings.ORDER_SESSION_ID] = self.menu_order
        self.session.modified = True

    def add(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.menu_order:
            self.menu_order[product_id] = 1

        else:
            temp = self.menu_order[product_id]
            self.menu_order[product_id] = temp + quantity
            print('THIS!', self.menu_order[product_id])

        if self.menu_order[product_id] == 0:
            self.remove(product_id)
        self.save()

    def remove(self, product_id):
        if product_id in self.menu_order:
            del self.menu_order[product_id]
            self.save()

    def get_total_cost(self):
        total_price = 0
        for key in self.menu_order.keys():
            item = Item.objects.get(pk=key)
            total_price += item.price * self.menu_order[key]

        return total_price / 100

    def get_order_quantity(self):
        quantity = 0
        for p in self.menu_order.values():
            quantity += int(p)

        return quantity

    def get_order_items(self):
        items = {}
        for key, value in self.menu_order.items():
            item = Item.objects.get(pk=key)
            items[item] = {'quantity': value}
        print(items)
        return items
