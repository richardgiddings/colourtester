from django import forms
from .models import ColourCombo

class ColourComboForm(forms.ModelForm):
    class Meta:
        model = ColourCombo
        fields = '__all__'