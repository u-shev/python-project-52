import json
from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User


class SetupTestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.create_url = reverse_lazy('create_user')
        self.update_pk1_url = reverse_lazy('update_user', kwargs={"pk": 1})
        self.delete_pk1_url = reverse_lazy("delete_user", kwargs={"pk": 1})
        self.delete_pk3_url = reverse_lazy("delete_user", kwargs={"pk": 3})
        self.login_url = reverse_lazy('login')
        self.users_url = reverse_lazy('users')
        self.users = User.objects.all()
        self.user1 = User.objects.get(pk=1)
        self.user3 = User.objects.get(pk=3)
        with open('task_manager/users/tests/fixtures/user.json') as file:
            self.test_user = json.load(file)


class TestCreateUser(SetupTestUser):

    def test_open_create_page(self):
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        response = self.client.post(path=self.create_url, data=self.test_user)
        self.assertRedirects(response, self.login_url, 302)
        self.user4 = User.objects.get(pk=5)
        self.assertEqual(first=self.user4.username,
                         second=self.test_user.get('username'))
        self.assertEqual(first=self.user4.first_name,
                         second=self.test_user.get('first_name'))
        self.assertEqual(first=self.user4.last_name,
                         second=self.test_user.get('last_name'))
