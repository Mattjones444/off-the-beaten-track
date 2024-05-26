from django.contrib import admin
from .models import Category,Activity

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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Activity, ActivityAdmin)
