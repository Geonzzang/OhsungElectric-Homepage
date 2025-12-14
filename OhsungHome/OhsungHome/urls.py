from django.contrib import admin
from django.urls import path, include
from OhsungHome import views

urlpatterns = [
    path("", include("mainpage.urls")),
    path("certi/", include("certificate_page.urls")),
    path("product/", include("product_page.urls")),
    path("admin/", admin.site.urls),
    
]
from django.conf.urls.static import static
from django.conf import settings


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from OhsungHome import views
# 404 error 가 발생시 해결 Setting에 debug == False로 바꿔줘야됨
handler404 = "OhsungHome.views.error_404_view"

