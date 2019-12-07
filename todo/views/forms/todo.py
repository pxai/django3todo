from django import forms
from django.forms import ModelForm
from .validators.validate_text import validate_text
from ...models.todo import Todo

class TodoForm(ModelForm):
    task = forms.CharField(initial='class',label='Task', max_length=100, min_length=3, validators=[validate_text])

    class Meta:
        model = Todo
        fields = ['task']