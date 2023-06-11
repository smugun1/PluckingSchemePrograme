from django import forms

from .models import ProgrammedScheme, RoundsMonitor, AutoFields, TeaPluckingCycle, FieldsToPluck


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


class CycleForms(forms.ModelForm):
    class Meta:
        model = TeaPluckingCycle
        fields = '__all__'


class FieldsForm(forms.ModelForm):
    class Meta:
        model = FieldsToPluck
        fields = '__all__'