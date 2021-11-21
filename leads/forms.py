from django import forms
from django.forms import fields
from .models import Agent, Lead


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
