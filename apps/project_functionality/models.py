from django.db import models

# from django.urls import reverse

from apps.project_functionality.services_prodject.get_content_from_page import get_some_content_from_page_main


# Create your models here.


# class Url(models.Model):
#     url = models.CharField(max_length=100)
#     address = models.CharField(max_length=100, default=None, null=True, blank=True)
#     phone = models.CharField(max_length=100, default=None, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class HelpPoint(models.Model):
    list_object = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        list_object = get_some_content_from_page_main()  # получаем список из другой функции
        # сохраняем список в поле list_object
        self.list_object = "\n".join(list_object)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.list_object}"

    __repr__ = __str__
