from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Category, Activity, Reviews
from .forms import ReviewForm
from .forms import ProductForm
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


def reviews(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id) 
    reviews = Reviews.objects.filter(activity_name_id=activity_id)
    
    
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.activity_name_id = activity_id
            review.save()
            messages.success(request, f"Thank you for leaving a review on {activity.name}")
            print(review)
            return redirect(reverse('reviews', args=[activity_id]))
        else:
            print("Form errors:", form.errors)
    else:
        form = ReviewForm()

    return render(request, 'activity/reviews.html', {'form': form, 'activity_id': activity_id, 'activity': activity, 'reviews': reviews})



@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('activity_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'activity/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, activity_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, pk=activity_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=activity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('activity_detail', args=[activity.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=activity)
        messages.info(request, f'You are editing {activity.name}')

    template = 'activity/edit_product.html'
    context = {
        'form': form,
        'activity': activity,
    }

    return render(request, template, context)


@login_required
def delete_product(request, activity_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    activity = get_object_or_404(Activity, pk=activity_id)
    activity.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('activity'))