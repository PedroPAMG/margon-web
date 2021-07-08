from django.contrib import admin
from .models import Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('key','title','order')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups == "Admin":
            return ('key', 'created', 'updated')
        else:
            return ('created', 'updated')

admin.site.register(Page, PageAdmin)
