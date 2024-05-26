from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category, Activity
from django.db.models.functions import Lower


def all_activity(request):
    """ A view to return the activity page """

    activity = Activity.objects.all()
    query = None
    categories = None
    country = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                activity = activity.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            activity = activity.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            activity = activity.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'country' in request.GET:
            country = request.GET['country'].split(',')
            activity = activity.filter(country__in=country)
            country = Activity.objects.filter(name__in=country)
            

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('activity'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            activity = activity.filter(queries)

    current_sorting = f'{sort}_{direction}'


    context = {
        "activity": activity,
        'search_term': query,
        'current_categories': categories,
        'country': country,
        'current_sorting': current_sorting,
    }


    return render(request, 'activity/activity.html', context)


def activity_detail(request, activity_id):
    """ A view to show individual activity details """

    activity = get_object_or_404(Activity, pk=activity_id)
    
    context = {
        'activity': activity,
    }

    return render(request, 'activity/activity_detail.html', context)
