from django.contrib import admin
from .models import RepositoryInfo


@admin.register(RepositoryInfo)
class RepositoryInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'branches', 'tags')
