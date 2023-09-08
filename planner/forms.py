from django import forms
from .models import Task
from datetime import date


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['end_date'].initial = date.today()

    class Meta:
        model = Task
        fields = ['title', 'task', 'status',  'end_date']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'task': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-control mb-3'}),
            'status': forms.Select(attrs={'class': 'form-select mb-3'})
        }


class ChangeTaskStatus(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']

        widgets={
            'status': forms.Select(attrs={'class': 'form-select mb-3'}),
            'end_date': forms.SelectDateWidget(attrs={'class': 'form-control mb-3'})
        }
