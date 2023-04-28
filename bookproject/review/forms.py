from django import forms
from .models import BookReview


class ReviewForm(forms.ModelForm):

    class Meta:
        model = BookReview
        fields = '__all__'