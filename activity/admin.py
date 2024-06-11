from django.contrib import admin
from .models import Category,Activity,Reviews

# Register your models here.

class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'sku',
        'name',
        'description',
        'country',
        'location',
        'price',
        'group_size',
        'rating',
        'duration',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
    

class ReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'activity_name',
        'id',
        'name',
        'review_rating',
        'review_description',
        'created'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Reviews, ReviewsAdmin)
