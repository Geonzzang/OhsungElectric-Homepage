from django.shortcuts import render, get_object_or_404
from django.http import FileResponse, Http404
from django.conf import settings
import os
from .models import CatalogFile

def catalog_list(request):
    """카탈로그 파일 목록 페이지"""
    files = CatalogFile.objects.filter(is_active=True)
    return render(request, 'catalog/catalog.html', {'files': files})

def download_file(request, file_id):
    """개별 파일 다운로드"""
    catalog_file = get_object_or_404(CatalogFile, id=file_id, is_active=True)
    
    if not catalog_file.file:
        raise Http404("파일을 찾을 수 없습니다.")
    
    file_path = catalog_file.file.path
    if not os.path.exists(file_path):
        raise Http404("파일이 존재하지 않습니다.")
    
    response = FileResponse(
        open(file_path, 'rb'),
        as_attachment=True,
        filename=catalog_file.name
    )
    return response
