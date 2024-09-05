from django import forms
from .models import User
from django.core.exceptions import ValidationError


# User Login Form
class UserLoginForm(forms.Form):
    email = forms.CharField()  # Email field for user authentication
    password = forms.CharField(
        widget=forms.PasswordInput
    )  # Password field for user authentication

    class Meta:
        model = User
        fields = ("email", "password")


# User Registration Form
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="password", widget=forms.PasswordInput
    )  # Password field for user registration
    password2 = forms.CharField(
        label="confirm password", widget=forms.PasswordInput
    )  # Confirm password field for user registration

    class Meta:
        model = User
        fields = ("email",)  # Email field for user registration

    # Method to validate password confirmation
    def clean_password2(self):
        cd = self.cleaned_data
        if (
                cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]):
            raise ValidationError("passwords don't match")
        return cd["password2"]

    # Method to validate email uniqueness
    def clean_email(self):
        email = self.cleaned_data["email"]
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError("This email already exists")
        return email

    # Method to save user registration form
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
