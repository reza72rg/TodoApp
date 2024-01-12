from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from todo.models import Task, Status


class TestTodoModels(TestCase):
    def setUp(self):
        self.status = Status.objects.create(name= 'test')
    def test_create_task_with_valid_data(self):
        task = Task.objects.create(
            title="test",
            description="test",
            status=self.status,
            )
      
        self.assertTrue(Task.objects.filter(pk=task.id).exists()) 
        #self.assertEqual(song.author.username,"test")
