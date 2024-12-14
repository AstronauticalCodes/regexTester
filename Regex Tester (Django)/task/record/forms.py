from .models import Record
from django import forms


class MainForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['regex', 'text', 'result']