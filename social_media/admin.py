from django.contrib import admin
from .models import Social_Media
# Register your models here.

class SocialMedialAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name','url')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups == "Admin":
            return ('created', 'updated')
        else:
            return ('created', 'updated')

admin.site.register(Social_Media, SocialMedialAdmin)