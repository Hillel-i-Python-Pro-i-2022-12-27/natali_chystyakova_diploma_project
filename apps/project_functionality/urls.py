from django.urls import path
from . import views

from django.contrib.auth.decorators import login_required

app_name = "project_functionality"

urlpatterns = [
    path("list/", views.HelpPointListView.as_view(), name="list"),
    path("update/<int:pk>/", login_required(views.HelpPointUpdateView.as_view()), name="update"),
    path("delete/<int:pk>/", login_required(views.HelpPointDeleteView.as_view()), name="delete"),
]
