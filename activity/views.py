from django.shortcuts import render, get_object_or_404
from .models import Category,Activity

def all_activity(request):
    """ A view to return the activity page """

    activity = Activity.objects.all()

    context = {
        "activity": activity,
    }


    return render(request, 'activity/activity.html', context)


def activity_detail(request, activity_id):
    """ A view to show individual activity details """

    activity = get_object_or_404(Activity, pk=activity_id)
    
    context = {
        'activity': activity,
    }

    return render(request, 'activity/activity_detail.html', context)
