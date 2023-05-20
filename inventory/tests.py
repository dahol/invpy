from django.test import TestCase
from .models import Item, Task, Project

# Create your tests here.

class ItemTestCase(TestCase):
    def setUp(self):
        self.item = Item.objects.create(
            name="Test Item",
            desc="This is a test item",
        )

class ProjectTestCase(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            desc="This is a test project",
        )

class TaskTestCase(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            name="Test Task",
            desc="This is a test task",
        )