from django import forms
from .models import Todo_Task


Status = [('In Progress', 'In Progress'), ('Complated', 'Complated'), ('Pending', 'Pending')]


class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = Todo_Task
        fields = ('task_name', 'task_description', 'task_deadline')

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'task_description': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'task_deadline': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date'
            }),

        }


class TaskUpdateForm(forms.ModelForm):

    class Meta:
        model = Todo_Task
        exclude = ('task_completed',)
        widgets = {
            "task_name": forms.TextInput(attrs={
                'class': 'form-control',
                'readonly': True,
            }),
            "task_description": forms.Textarea(attrs={
                'class': 'form-control',
                'readonly': True,
            }),
            "task_status": forms.Select(attrs={
                'class': 'form-select',
            }),
            "task_deadline": forms.DateInput(attrs={
                'class': 'form-control',
                'readonly': True,
                'type': 'date'
            })
        }
