from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from todo.views import Tasklist, TaskUpdate
# Create your tests here.


class TestUrl(TestCase):
    
    def test_todo_index_url_resolve(self):
        url = reverse('todo:task_list')
        self.assertEquals(resolve(url).func.view_class, Tasklist)
           
    def test_todo_update_url_resolve(self):
        url = reverse('todo:update_task',kwargs={'pk':10})
        self.assertEquals(resolve(url).func.view_class, TaskUpdate)