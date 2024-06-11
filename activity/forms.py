from django import forms
from .models import Reviews

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'review_rating', 'review_description']