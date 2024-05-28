from django.shortcuts import render, redirect
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from activity.models import Category, Activity
from datetime import datetime

# Create your views here.

def grand_total(request):
    """ A view that renders the bag contents page """

    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0
    # bag = request.session.get('bag', {})
    grand_total = 0

    for item_id, item_data in bag.items():
        activity = get_object_or_404(Activity, pk=item_id)
        # date = request.POST.get('datepickerfrom')
        if isinstance(item_data, int):
            # Handle legacy integer quantity format
            quantity = item_data
            date = ''
            # Update the session to use the dictionary format
            bag[item_id] = {'quantity': quantity, 'date': date}
        else:
            quantity = item_data['quantity']
            date = item_data.get('date', '')
        total += quantity * activity.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'activity': activity,
            'date': date,
        })
    request.session['bag'] = bag
    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'free_activity_threshold': settings.FREE_ACTIVITY_THRESHOLD,
        'grand_total': grand_total,
        # 'date': date,
    }
    
    return context

    