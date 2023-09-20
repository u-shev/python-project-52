from django.test import TestCase
from statuses.models import Status


class StatusesTest(TestCase):

    def setUp(self):
        Status.objects.create(name="first",)
        Status.objects.create(name="second",)

    def test_create_status(self):
        new = Status.objects.create(name="new")
        self.assertEqual(new.name, "new")

    def test_update_status(self):
        first = Status.objects.get(name="first")
        first.name = "changed"
        self.assertNotEqual(first.name, "first")

    def test_delete_status(self):
        second = Status.objects.get(name="second")
        second.delete()
        self.assertEqual(second.id, None)
