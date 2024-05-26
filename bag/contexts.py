from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < settings.FREE_ACTIVITY_THRESHOLD:
        grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'free_activity_threshold': settings.FREE_ACTIVITY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

