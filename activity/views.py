from django.shortcuts import render
from .models import Category,Activity

def all_activity(request):
    """ A view to return the activity page """

    activity = Activity.objects.all()

    context = {
        "activity": activity,
    }


    return render(request, 'activity/activity.html', context)
