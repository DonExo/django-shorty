from django import forms
from .models import Shortener as ModelShortener


class FormShortener(forms.ModelForm):
    original_url = forms.URLField(label="URL Field", widget=forms.TextInput(attrs={'placeholder': 'Your LOOOONG url here'}))

    class Meta:
        model = ModelShortener
        fields = ('original_url', )