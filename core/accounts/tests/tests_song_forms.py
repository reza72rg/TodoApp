from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from accounts.forms import UserCreationForm
# Create your tests here.
class TestAccountsForm(TestCase):
    def test_accounts_form_with_vaild_data(self):
        form = UserCreationForm(data={
            'email':"test@gmail.com",
            'password1':'123456789ab',
            'password2':'123456789ab',
        })
        self.assertTrue(form.is_valid())
    
    def test_accounts_form_with_no_data(self):
        form = UserCreationForm(data={})
        self.assertFalse(form.is_valid())