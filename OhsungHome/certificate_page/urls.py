from django.urls import path, include

from . import views


app_name = "certificate_page"

urlpatterns = [
    path('', views.certi_render, name='certi'),
]