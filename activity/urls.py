from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_activity, name='activity'),
    path('<activity_id>', views.activity_detail, name='activity_detail'),
]