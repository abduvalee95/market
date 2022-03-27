from django.db import models

# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=255, blank=True,null=True)
    describtion = models.TextField(blank=True,null=True)
    # logo = models.ImageField(upload_to='logo/',blank=True,null=True)

    
    def __str__(self):   # Это возврошает по title не по id в админ
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"