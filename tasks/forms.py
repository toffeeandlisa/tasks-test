from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'relevance']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Write a title'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write a description'}),
            'relevance': forms.CheckboxInput(attrs={'class':'form-check-input m-auto mb-3'})
        }