from django import forms
from django.forms import fields
from .models import Agent, Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField  # Import to make a custom user creation form
from django.contrib.auth import get_user_model

User = get_user_model()

# Django Forms
class LeadForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=10)
    agent = forms.ModelChoiceField(queryset=Agent.objects.all())


# Model forms
class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        # fields = ['fist_name', 'last_name', 'age', 'agent']
        fields = '__all__'


# Custom user creation model
class CustomUserCreationForm(UserCreationForm):
    """ Custom user creation model to set the Meta model to custom user model.
        Otherwise it will call the default django user model, which is not exist.
    """
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
