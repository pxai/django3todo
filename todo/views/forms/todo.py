from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(label='Task', max_length=100)