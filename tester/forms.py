from django import forms
from .models import ColourCombo
import re

class ColourComboForm(forms.ModelForm):
    class Meta:
        model = ColourCombo
        fields = '__all__'

    def clean_bgcolour_one(self):
        data = self.cleaned_data['bgcolour_one']
        if not self.is_hex(data):
            raise forms.ValidationError("Invalid background colour")
        return data

    def clean_bgcolour_two(self):
        data = self.cleaned_data['bgcolour_two']
        if not self.is_hex(data):
            raise forms.ValidationError("Invalid background colour")
        return data

    def clean_textcolour_one(self):
        data = self.cleaned_data['textcolour_one']
        if not self.is_hex(data):
            raise forms.ValidationError("Invalid text colour")
        return data

    def clean_textcolour_two(self):
        data = self.cleaned_data['textcolour_two']
        if not self.is_hex(data):
            raise forms.ValidationError("Invalid text colour")
        return data

    def is_hex(self, val):
        pattern = re.compile("[#]([0-9A-Fa-f]{6})")
        if pattern.fullmatch(val) is None:
            return False
        return True