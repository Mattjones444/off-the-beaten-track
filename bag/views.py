from django.shortcuts import render, redirect
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from activity.models import Category, Activity
from datetime import datetime

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    product_count = 0
    # bag = request.session.get('bag', {})
    # grand_total = 0

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

    return render(request, 'bag/bag.html', context)


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    if request.method == "POST":
        quantity = int(request.POST.get('quantity'))
        date = request.POST.get('datepickerfrom')
        redirect_url = request.POST.get('redirect_url') or 'view_bag'
        bag = request.session.get('bag', {})

        if item_id in bag:
            if isinstance(bag[item_id], int):
                # If the existing item is an integer, update to dictionary format
                bag[item_id] = {'quantity': bag[item_id] + quantity, 'date': date}
            else:
                bag[item_id]['quantity'] += quantity
                bag[item_id]['date'] = date  # Update the date
        else:
            bag[item_id] = {'quantity': quantity, 'date': date}

        request.session['bag'] = bag
        print(bag)
        return redirect(redirect_url)
    else:
        return redirect('view_bag')