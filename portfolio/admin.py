from django.contrib import admin
from django.contrib.admin.filters import RelatedOnlyFieldListFilter
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project, ProjectAdmin)
