from django.views.generic import ListView, UpdateView, DeleteView


from django.urls import reverse_lazy

from apps.project_functionality.models import HelpPoint


class HelpPointListView(ListView):
    model = HelpPoint

    queryset = HelpPoint.objects.all().order_by("created_at")


class HelpPointUpdateView(UpdateView):
    model = HelpPoint
    fields = ("list_object",)
    success_url = reverse_lazy("contacts:list_by_class")


class HelpPointDeleteView(DeleteView):
    model = HelpPoint

    success_url = reverse_lazy("contacts:list_by_class")
