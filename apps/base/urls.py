from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path("about/", views.AboutUsView.as_view(), name="about_us"),
]
