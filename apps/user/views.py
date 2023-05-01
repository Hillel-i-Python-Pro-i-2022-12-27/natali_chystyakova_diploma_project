from pyexpat.errors import messages

from django.shortcuts import redirect
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


User = get_user_model()


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={"class": "form-input"}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "avatar",
        )


class SignUpView(CreateView):
    # form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("root:index")


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "registration/login.html"


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    # return redirect("root:index")


class UserUpdateView(UpdateView):
    model = User

    template_name = "registration/edit.html"
    fields = (
        "username",
        "email",
        "avatar",
    )
    success_url = reverse_lazy("root:index")


class UserDetailView(DetailView):
    model = User
