from django import forms
from .models import TaskModel

class TaskModelForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['task',]


class TaskUpadateForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'