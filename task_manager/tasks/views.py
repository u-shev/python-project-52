from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, \
    UpdateView, DeleteView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import UserLoginRequiredMixin, DeleteProtectionMixin
from .models import Task
from .forms import TaskForm

class TasksListView(UserLoginRequiredMixin, ListView):

    template_name = 'tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'
    extra_context = {
        'title': _( 'Tasks')
    }


class TaskDetailView(UserLoginRequiredMixin,
                       SuccessMessageMixin, DetailView):
    model = Task
    template_name = "tasks/task.html"
    context_object_name = "task"
    extra_context = {'title': _('Task view'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class TaskCreateView(UserLoginRequiredMixin,
                       SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy( 'tasks')
    success_message = _( 'Task successfully created')
    extra_context = {
        'title': _('Create Task'),
        'button_text': _('Create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskUpdateView(UserLoginRequiredMixin,
                       SuccessMessageMixin, UpdateView):

    template_name = 'form.html'
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('Task updated')
    extra_context = {
        'title': _('Update Task'),
        'button_text': _('Update'),
    }


class TaskDeleteView(UserLoginRequiredMixin, DeleteProtectionMixin,
                       SuccessMessageMixin, DeleteView):

    template_name =  'tasks/delete.html'
    model = Task
    success_url = reverse_lazy('tasks')
    success_message = _('Task deleted')
    protected_message = _('You cannot delete staus while it is in use')
    protected_url = reverse_lazy( 'tasks')
    extra_context = {
        'title': _('Delete Task'),
        'button_text': _('Yes, delete'),
    }
