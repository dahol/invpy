from django.test import TestCase

# Create your tests here.

class ItemTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name="Itemtest1", desc="Itemtest desc1")
        Item.objects.create(name="Itemtest2", desc="Itemtest desc2")
        
class TaskTestCase(TestCase):
    def setUp(self):
        Task.objects.create(name="Tasktest1", desc="Tasktest desc1")
        Task.objects.create(name="Tasktest2", desc="Tasktest desc2")

