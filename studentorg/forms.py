from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={
        'placeholder': 'Search organizations...',
        'class': 'form-control'
    }))
