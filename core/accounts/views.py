from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect

# Custom Login View
class CustomLoginView(LoginView):
    template_name = "accounts/login.html"  # Template for the login page
    fields = "username", "password"  # Fields to display on the login form
    redirect_authenticated_user = True  # Redirect to success URL if user is already authenticated

    def get_success_url(self):
        return reverse_lazy("todo:task_list")  # Redirect to the task list page after successful login

# Register Page View
class RegisterPage(FormView):
    template_name = "accounts/register.html"  # Template for the registration page
    form_class = UserCreationForm  # Form class for user registration
    redirect_authenticated_user = True  # Redirect to success URL if user is already authenticated
    success_url = reverse_lazy("todo:task_list")  # Redirect to the task list page after successful registration

    def form_valid(self, form):
        user = form.save()  # Save the user registration form
        if user is not None:
            login(self.request, user)  # Log in the user after successful registration
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todo:task_list")  # Redirect to the task list page if user is already authenticated
        return super(RegisterPage, self).get(*args, **kwargs)