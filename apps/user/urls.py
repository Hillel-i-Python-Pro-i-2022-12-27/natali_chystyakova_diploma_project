from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = "user"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("update_u/<int:pk>/", login_required(views.UserUpdateView.as_view()), name="update_u"),
    path("logout", views.logout_request, name="logout"),
    path("profile/<int:pk>", views.UserDetailView.as_view(), name="profile"),
]
