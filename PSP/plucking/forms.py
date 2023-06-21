from django import forms

from .models import ProgrammedScheme, RoundsMonitor, AutoFields, GrowingCycle, DivisionDetails


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


class FieldsForms(forms.ModelForm):
    class Meta:
        model = AutoFields
        fields = '__all__'


class GrowingCycleForms(forms.ModelForm):
    class Meta:
        model = GrowingCycle
        fields = '__all__'


class DivisionZonesForms(forms.ModelForm):
    class Meta:
        model = DivisionDetails
        fields = '__all__'
