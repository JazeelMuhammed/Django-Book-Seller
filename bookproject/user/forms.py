from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.apps import apps


class AbstractUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditForm(forms.ModelForm):

    class Meta:
        model = apps.get_model('book', 'Book')
        fields = '__all__'