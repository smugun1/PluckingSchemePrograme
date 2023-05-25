from django import forms

from .models import Resources, ProgrammedScheme, RoundsMonitor


class ResourcesForm(forms.ModelForm):
    class Meta:
        model = Resources
        fields = '__all__'


class PSPForms(forms.ModelForm):
    class Meta:
        model = ProgrammedScheme
        fields = '__all__'


class ProgrammedSchemeForm(forms.ModelForm):
    class Meta:
        model = ProgrammedScheme
        fields = '__all__'


class RoundsMonitorForm(forms.ModelForm):
    class Meta:
        model = RoundsMonitor
        fields = '__all__'
