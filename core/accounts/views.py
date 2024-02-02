# Import necessary modules
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect
from accounts.forms import UserCreationForm


# Custom Login View
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    # Template for the login page
    fields = "username", "password"
    # Fields to display on the login form
    redirect_authenticated_user = (
        True
        # Redirect to success URL if user is already authenticated
    )

    def get_success_url(self):
        return reverse_lazy("todo:task_list")
        # Redirect to the task list page after successful login


class RegisterPage(CreateView):
    template_name = (
        "accounts/register.html"
        # Template for the registration page
    )
    form_class = UserCreationForm
    # Form class for user registration
    redirect_authenticated_user = (
        True
        # Redirect to success URL if user is already authenticated
    )
    success_url = reverse_lazy("todo:task_list")
    # Redirect to the task list page after successful registration

    def form_valid(self, form):
        user = form.save()
        # Save the user registration form
        if user is not None:
            login(self.request, user)
            # Log in the user after successful registration
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todo:task_list")
            # Redirect to the task list page if user is already authenticated
        return super(RegisterPage, self).get(*args, **kwargs)
    
    
    
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from .tasks import Send_email
from django.core.cache import cache
def send_email(request):
    Send_email.delay()
    return HttpResponse("<h1>Done Sending</h1>")
import requests
'''def test(request):
    if cache.get("test_delay_api") is None:
        response = requests.get('https://9b27fe39-f4e4-4740-853a-712190ec90b6.mock.pstmn.io/test/delay5')
        cache.set("test_delay_api",response.json(),60)
    return JsonResponse(cache.get("test_delay_api"))'''

@cache_page(60)
def test(request):
    response = requests.get('https://9b27fe39-f4e4-4740-853a-712190ec90b6.mock.pstmn.io/test/delay5')
    return JsonResponse(response.json())