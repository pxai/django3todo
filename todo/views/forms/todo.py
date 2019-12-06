from django import forms
from .validators.validate_text import validate_text

class TodoForm(forms.Form):
    task = forms.CharField(initial='class',label='Task', max_length=100, min_length=3, validators=[validate_text])

