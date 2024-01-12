from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from todo.forms import TaskForm
# Create your tests here.
class TestTodoForm(TestCase):
    def test_todo_form_with_vaild_data(self):    
        form = TaskForm(data={
        "title":"test",
        "description":"test",
        "status":"test",
        })
        self.assertTrue(form.is_valid())
    def test_todo_form_with_no_data(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())