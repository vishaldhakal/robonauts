from django.db import models
from ckeditor.fields import RichTextField

class blog(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=500)
    tags = models.CharField(max_length=300)
    meta_title = models.CharField(max_length=150)
    meta_description = models.CharField(max_length=400)
    meta_keyword = models.CharField(max_length=200)
    thumbnail_image = models.FileField()
    content = RichTextField(blank=True,null=True)

    def __str__(self):
        return self.title
