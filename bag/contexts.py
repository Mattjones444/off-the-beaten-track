from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from activity.models import Category, Activity
from datetime import datetime

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    grand_total = 0

    for item_id, quantity in bag.items():
        activity = get_object_or_404(Activity, pk=item_id)
        total += quantity * activity.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'activity': activity,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'free_activity_threshold': settings.FREE_ACTIVITY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

