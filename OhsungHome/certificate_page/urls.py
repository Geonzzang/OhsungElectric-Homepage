from django.urls import path, include

from . import views


app_name = "certificate_page"

urlpatterns = [
    path('', views.render_page, name='certi'),
]