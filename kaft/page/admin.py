from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = (
      'page_name',
      'description',
      'status'
    )


admin.site.register(Page, PageAdmin)
