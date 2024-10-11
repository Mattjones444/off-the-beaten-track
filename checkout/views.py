from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import Http404
from .forms import OrderForm
from .models import Order, OrderLineItem
from activity.models import Activity
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from bag.contexts import grand_total
import stripe
import json
from decimal import Decimal

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            try:
                order = order_form.save()

                for item_id, item_data in bag.items():
                    try:
                        activity = Activity.objects.get(id=item_id)

                        # Check if the price of the activity is negative
                        if activity.price < 0:
                            messages.error(request, (
                                f"The product {activity.name} has an invalid price of {activity.price}. "
                                "Please contact customer support.")
                            )
                            order.delete()
                            return redirect(reverse('view_bag'))

                        if isinstance(item_data, int):
                            order_line_item = OrderLineItem(
                                order=order,
                                activity=activity,
                                quantity=item_data,
                            )
                            order_line_item.save()
                        else:
                            quantity = item_data['quantity']

                            # Convert and validate quantity
                            if isinstance(quantity, str):
                                if quantity.isdigit():
                                    quantity = int(quantity)
                                else:
                                    raise ValueError(f"Invalid quantity value (string): {quantity}")
                            elif isinstance(quantity, (float, Decimal)):
                                quantity = int(quantity)
                            elif isinstance(quantity, int):
                                pass
                            else:
                                raise ValueError(f"Invalid quantity type: {type(quantity)}")

                            order_line_item = OrderLineItem(
                                order=order,
                                activity=activity,
                                quantity=quantity,
                            )
                            order_line_item.save()

                    except Activity.DoesNotExist:
                        messages.error(request, (
                            "One of the products in your bag wasn't found in our database. "
                            "Please call us for assistance!")
                        )
                        order.delete()
                        return redirect(reverse('view_bag'))

                request.session['save_info'] = 'save-info' in request.POST
                return redirect(reverse('checkout_success', args=[order.order_number]))

            except Exception as e:
                messages.error(request, f'An error occurred while processing your order: {str(e)}')
                return redirect(reverse('view_bag'))

        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')

    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('activity'))

        # Calculate the current bag total
        current_bag = grand_total(request)
        total = current_bag['grand_total']

        # Check if the total is less than 1
        if total < 1:
            messages.error(request, "The total amount must be greater than 0 to proceed to checkout.")
            return redirect(reverse('view_bag'))

        # Calculate stripe total in cents
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key

        # Create a payment intent with Stripe
        try:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
        except stripe.error.InvalidRequestError as e:
            messages.error(request, "There was an issue with the payment process. Please try again later.")
            return redirect(reverse('view_bag'))
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")
            return redirect(reverse('view_bag'))

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                })
            except UserProfile.DoesNotExist:
                raise Http404("Profile not found")

        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret if intent else None,
    }
    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    try:
        save_info = request.session.get('save_info')
        order = get_object_or_404(Order, order_number=order_number)
        messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')
        
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            # Attach the user's profile to the order
            order.user_profile = profile
            order.save()
            # Save the user's info
            if save_info:
                profile_data = {
                    'default_phone_number': order.phone_number,
                    'default_country': order.country,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                }
                user_profile_form = UserProfileForm(profile_data, instance=profile)
                if user_profile_form.is_valid():
                    user_profile_form.save()
        
        if 'bag' in request.session:
            del request.session['bag']

        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
        }
        return render(request, template, context)
    
    except Order.DoesNotExist:
        raise Http404("Order not found")
    except PermissionDenied:
        raise PermissionDenied("You do not have permission to access this order.")
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {str(e)}")
        return redirect(reverse('view_bag'))
