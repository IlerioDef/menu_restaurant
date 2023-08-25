from .order import Order


def order(request):
    return {'menu_order': Order(request)}
