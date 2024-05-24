from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Category,Activity


def all_activity(request):
    """ A view to return the activity page """

    activity = Activity.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('activity'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            activity = activity.filter(queries)

            print(activity)

    context = {
        "activity": activity,
        'search_term': query,
    }


    return render(request, 'activity/activity.html', context)


def activity_detail(request, activity_id):
    """ A view to show individual activity details """

    activity = get_object_or_404(Activity, pk=activity_id)
    
    context = {
        'activity': activity,
    }

    return render(request, 'activity/activity_detail.html', context)
