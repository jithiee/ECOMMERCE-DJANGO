from django import forms
from Home.models import Vehicle


class Carforms(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'