from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path('', views.catalog_list, name='catalog_list'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
]

