from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.views.generic import TemplateView


def index(request: WSGIRequest):
    return render(
        request=request,
        template_name="index.html",
    )


class AboutUsView(TemplateView):
    template_name = "base/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "about_us"

        return context
