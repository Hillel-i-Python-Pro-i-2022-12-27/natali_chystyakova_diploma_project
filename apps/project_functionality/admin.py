from django.contrib import admin
from . import models


# admin.site.register(models.Contact)


@admin.register(models.HelpPoint)
class HelpPointAdmin(admin.ModelAdmin):
    list_display = (
        "list_object",
        "created_at",
    )


class ContactInline(admin.TabularInline):
    model = models.HelpPoint
