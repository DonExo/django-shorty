from django import forms
from .models import Shortener as ModelShortener


class FormShortener(forms.ModelForm):
    class Meta:
        model = ModelShortener
        fields = ('original_url', )