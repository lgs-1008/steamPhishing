from django import forms
from .models import Form

class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['username', 'password']
