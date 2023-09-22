from django import forms
from django.utils.translation import gettext as _

from .models import Status


class StatusForm(forms.ModelForm):

    class Meta:
        model = Status
        fields = ('name',)
