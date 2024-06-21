from django.test import TestCase
from .forms import OrderForm
from .models import Order


from django.test import TestCase
from .forms import OrderForm



class TestOrderForm(TestCase):

    def test_set_up(self):
        self.valid_data = {
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4B',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'US'
        }


    def test_order_form_invalid_data(self):
        self.valid_data = {
            'full_name': 'John Doe',
            'email': 'johndoe@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4B',
            'town_or_city': 'Anytown',
            'postcode': '12345',
            'country': 'US'
        }
        invalid_data = self.valid_data.copy()
        invalid_data['email'] = 'not-an-email'
        form = OrderForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    

    
