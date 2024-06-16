from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_activity, name='activity'),
    path('<activity_id>', views.activity_detail, name='activity_detail'),
    path('<int:activity_id>/', views.reviews, name='reviews'),
    path('add/', views.add_product, name='add_product'),
]