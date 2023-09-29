from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.users.models import User


class TestLogout(TestCase):

    fixtures = ['users.json']

    def test_logout(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user=user)
        response = self.client.post(
            reverse_lazy('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertFalse(response.context['user'].is_authenticated)
