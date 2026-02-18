from django import forms
from django.forms import ModelForm
from .models import Organization


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={
        'placeholder': 'Search organizations...',
        'class': 'form-control'
    }))


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = '__all__'
