from django.db import models
from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Activity(models.Model):

    class Meta:
        verbose_name_plural = 'Activities'


    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    country = models.CharField(max_length=254)
    location = models.CharField(max_length=254, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    group_size = models.IntegerField(null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    duration = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name



class Reviews(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    activity_name = models.ForeignKey('Activity', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=True)
    review_rating = models.IntegerField()
    review_description = models.CharField(max_length=500, default=None, null=False, blank=False)
    created = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
