from django import forms

from .models import Resources


class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = '__all__'