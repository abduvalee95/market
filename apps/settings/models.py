from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255)
    describtion = models.TextField()
    logo = models.ImageField(upload_to='logo/')
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    youtube = models.CharField(max_length=255)

    def __str__(self):   # Это возврошает по title не по id в админ
        return self.title


    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"
