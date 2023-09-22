from django import forms
from django.utils.translation import gettext as _

from .models import Label


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ('name',)
