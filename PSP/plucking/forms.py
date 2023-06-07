from django import forms

from .models import ProgrammedScheme, RoundsMonitor, FieldsToPluck, AutoFields


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


class FieldsForm(forms.ModelForm):
    class Meta:
        model = FieldsToPluck
        fields = '__all__'


class FieldsForms(forms.ModelForm):
    class Meta:
        model = AutoFields
        fields = '__all__'
