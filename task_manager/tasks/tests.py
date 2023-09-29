from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from django.urls import reverse_lazy


class TestTaskCreate(TestCase):

    fixtures = ['labels.json', 'users.json', 'tasks.json', 'statuses.json']

    def test_create_logout(self):
        response = self.client.get(reverse_lazy('create_task'))
        self.assertEqual(response.status_code, 302)

    def test_create_task(self):
        user = User.objects.get(pk=1)
        status = Status.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy('create_task'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 2)
        response = self.client.post(
            reverse_lazy('create_task'),
            {'name': 'task',
             'author': user.id,
             'status': status.id
             }
        )
        task = Task.objects.get(pk=3)
        self.assertEqual(Task.objects.all().count(), 3)
        self.assertEqual(task.__str__(), task.name)


class TestUpdateTask(TestCase):

    fixtures = ['labels.json', 'users.json', 'tasks.json', 'statuses.json']

    def test_update_logout(self):
        response = self.client.get(reverse_lazy('update_task', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_task_update(self):
        user1 = User.objects.get(pk=1)
        user2 = User.objects.get(pk=2)
        status = Status.objects.all().first()
        self.client.force_login(user=user1)
        response = self.client.get(reverse_lazy('update_task', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        new_task = {
            'name': 'task',
            'status': status.id,
            'executor': user2.id,
        }
        response = self.client.post(
            reverse_lazy('update_task', kwargs={'pk': 1}), new_task)
        status = Task.objects.get(pk=1)
        self.assertEqual(status.name, 'task')


class TestDeleteTask(TestCase):

    fixtures = ['labels.json', 'users.json', 'tasks.json', 'statuses.json']

    def test_delete_logout(self):
        response = self.client.get(reverse_lazy('delete_task', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)

    def test_delete_task(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy('delete_task', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse_lazy('delete_task', kwargs={'pk': 1})
        )
        self.assertEqual(Task.objects.all().count(), 1)


class DeleteConnectedStatus(TestCase):

    fixtures = ['labels.json', 'users.json', 'tasks.json', 'statuses.json']

    def test_delete_with_conn(self):
        task = Task.objects.get(pk=1)
        user = User.objects.get(pk=1)
        self.assertEqual(Task.objects.all().count(), 2)
        self.client.force_login(user=user)
        self.client.get(reverse_lazy('delete_task',
                        kwargs={'pk': task.id}))
        self.assertEqual(Task.objects.all().count(), 2)


class TestTasksList(TestCase):

    fixtures = ['labels.json', 'users.json', 'tasks.json', 'statuses.json']

    def test_list_logout(self):
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)

    def test_list_login(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_filter_tasks(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.get(
            reverse_lazy('tasks'),
            {'executor': 1}
        )

        self.assertEqual(response.context['tasks'].count(), 1)
