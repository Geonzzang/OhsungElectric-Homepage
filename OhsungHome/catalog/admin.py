from django.contrib import admin
from .models import CatalogFile

@admin.register(CatalogFile)
class CatalogFileAdmin(admin.ModelAdmin):
    list_display = ['name', 'file_type', 'is_active', 'created_at']
    list_filter = ['file_type', 'is_active', 'created_at']
    search_fields = ['name', 'description']
    list_editable = ['is_active']
