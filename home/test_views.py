from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from activity.models import Activity



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.activity = Activity.objects.create(name='Test Activity', description='Test Description')
        self.item_id = self.activity.id

   
    def test_homepage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


    def test_add_to_bag(self):
        item_id = Activity.id
        url = reverse('add_to_bag', args=[self.item_id])
        response = self.client.post(url, {'quantity': 1, 'datepickerfrom': '2024-06-21'})

        self.assertEqual(response.status_code, 302)


