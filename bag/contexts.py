from django.shortcuts import get_object_or_404
from developers.models import Developer


def bag_contents(request):
    """" Try/Except block to catch if a developer has been deleted whilst in user bag to prevent session 404"""

    bag_items = []
    total = 0
    bag_item_count = 0
    bag = request.session.get("bag", {})
    try:
        for item_id, quantity in bag.items():
            developer = get_object_or_404(Developer, pk=item_id)
            total = quantity * developer.rate
            bag_item_count = quantity
            bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": quantity,
                    "developer": developer,
                }
            )

        context = {
            "bag_items": bag_items,
            "total": total,
            "bag_item_count": bag_item_count,
        }

    except Exception:
        del request.session["bag"]
        context = {
            "bag_items": "",
            "total": 0,
            "bag_item_count": 0,
        }

    return context
