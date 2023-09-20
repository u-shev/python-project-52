from django.urls import reverse_lazy
from task_manager.mixins import UserPermissionMixin, \
    UserLoginRequiredMixin, DeleteProtectionMixin
from .forms import UserForm
from .models import User
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class UsersListView(ListView):

    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'
    extra_context = {
        'title': _('Users')
    }


class UserCreateView(SuccessMessageMixin, CreateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')
    extra_context = {
        'title': _('Create user'),
        'button_text': _('Register'),
    }


class UserUpdateView(UserLoginRequiredMixin, SuccessMessageMixin,
                     UserPermissionMixin, UpdateView):

    template_name = 'form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('users')
    success_message = _('User is successfully updated')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    extra_context = {
        'title': _('Update user'),
        'button_text': _('Update'),
    }


class UserDeleteView(UserLoginRequiredMixin, UserPermissionMixin,
                     DeleteProtectionMixin, SuccessMessageMixin, DeleteView):

    template_name = 'users/delete.html'
    model = User
    success_url = reverse_lazy('users')
    success_message = _('User is successfully deleted')
    permission_message = _('You have no rights to change another user.')
    permission_url = reverse_lazy('users')
    protected_message = _('Unable to delete a user because he is being used')
    protected_url = reverse_lazy('users')
    extra_context = {
        'title': _('Delete user'),
        'button_text': _('Yes, delete'),
    }
