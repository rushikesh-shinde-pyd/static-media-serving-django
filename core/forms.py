from django import forms
from .models import Fish


class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = '__all__'

