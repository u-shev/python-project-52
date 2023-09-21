from django import forms
from django.utils.translation import gettext as _

from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('name', 'description', 'status', 'executor')
        