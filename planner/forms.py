from django import forms
from .models import Task


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task', 'status',  'end_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'task': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-select mb-3 '}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'})
        }
