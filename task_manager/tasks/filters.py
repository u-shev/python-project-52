from requests import request
from .models import Task
from django_filters import FilterSet, filters, BooleanFilter
from task_manager.labels.models import Label
from django import forms
from django.utils.translation import gettext_lazy as _



class TaskFilter(FilterSet):
    labels = filters.ModelChoiceFilter(queryset=Label.objects.all())
    self_tasks = filters.BooleanFilter(label=_('Self tasks'), method='get_self_tasks',
                                       lookup_expr='isnull',
                                       widget=forms.CheckboxInput)

    def get_self_tasks(self, queryset, name, value):
        lookup = queryset.filter(author=self.request.user)
        return lookup if value else queryset


    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels', 'self_tasks']