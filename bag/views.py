from django.shortcuts import render,redirect
from datetime import datetime



def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    date = request.POST.get('datepickerfrom')
    if date:
        try:
            date_obj = datetime.strptime(date,'%Y-%m-%d').date()
            print(date_obj)
        except ValueError:
            print("Incorrect date format")

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(bag)
    return redirect(redirect_url)
