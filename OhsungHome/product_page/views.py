from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product_page/product.html"   # 템플릿 경로
    context_object_name = "products"                  # HTML에서 변수명
    ordering = ["-id"]                                # 최신순 정렬
    

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_page/product_detail.html"
    context_object_name = "product"


