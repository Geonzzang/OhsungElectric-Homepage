from django.db import models

class CatalogFile(models.Model):
    name = models.CharField(max_length=200, verbose_name="파일명")
    description = models.TextField(blank=True, verbose_name="설명")
    file = models.FileField(
        upload_to='catalog/',
        verbose_name="파일"
    )
    file_type = models.CharField(
        max_length=50,
        choices=[
            ('pdf', 'PDF'),
            ('image', '이미지'),
            ('other', '기타'),
        ],
        default='other',
        verbose_name="파일 유형"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="생성일")
    is_active = models.BooleanField(default=True, verbose_name="활성화")

    class Meta:
        verbose_name = "카탈로그 파일"
        verbose_name_plural = "카탈로그 파일들"
        ordering = ['-created_at']

    def __str__(self):
        return self.name
