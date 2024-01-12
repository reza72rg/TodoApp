from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from todo.views import Tasklist, TaskUpdate
from todo.models import Task, Status
from accounts.models import User
# Create your tests here.


class TestTodoView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="test@gmail.com",
            password='123456789ab')
        self.status = Status.objects.create(name= 'test')
        self.task = Task.objects.create(
                title="test",
                description="test",
                status=self.status,
        )
    def test_todo_index_url_successful_response(self):
        url = reverse('todo:task_list')
        response = self.client.get(url,follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("index"))
        # self.assertTemplateUsed(response, template_name = "list_task.html")    
    def test_todo_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('todo:update_task', kwargs={'pk':self.task.id})
        response = self.client.get(url)    
        self.assertEquals(response.status_code, 200)
    
    def test_todo_post_detail_anonymous_response(self):
        url = reverse('todo:update_task', kwargs={'pk':self.task.id})
        response = self.client.get(url, follow=True)    
        self.assertEquals(response.status_code, 200)
          