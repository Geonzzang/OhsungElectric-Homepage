from django.urls import path, include

from . import views
from .views import ProductListView, ProductDetailView

app_name = "product_page"

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]


