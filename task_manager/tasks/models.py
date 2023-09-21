from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.users.models import User
from task_manager.statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=150, blank=False, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))
    executor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,
        default='', related_name='executors', verbose_name=_('Executor'))
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False,
        related_name='authors', verbose_name=_('Author'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False,
        related_name='statuses', verbose_name=_('Status'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
