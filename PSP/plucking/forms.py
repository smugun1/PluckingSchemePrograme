from django import forms
from .models import PluckingRequirements, PluckingRounds, TeaPluckingPlannerSaveData


class PluckingForms(forms.ModelForm):
    content = forms.CharField(label='SimKMN', widget=forms.TextInput(
        attrs={'placeholder': 'Add task here...'}))

    class Meta:
        model = PluckingRequirements
        fields = '__all__'


class RoundsForms(forms.ModelForm):
    content = forms.CharField(label='SimKMN', widget=forms.TextInput(
        attrs={'placeholder': 'Add task here...'}))

    class Meta:
        model = PluckingRounds
        fields = '__all__'


class DataForm(forms.ModelForm):
    content = forms.CharField(label='SimKMN', widget=forms.TextInput(
        attrs={'placeholder': 'Add task here...'}))

    class Meta:
        model = TeaPluckingPlannerSaveData
        fields = '__all__'
