from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='products/', 
        null=True, 
        blank=True, 
        default=None
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        



