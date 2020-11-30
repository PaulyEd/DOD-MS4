from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    bag_item_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'bag_item_count': bag_item_count,
    }

    return context