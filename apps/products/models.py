from django.db import models
from apps.categories.models import Categories

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=255, blank=True,null=True)
    describtion = models.TextField(blank=True,null=True)
    # logo = models.ImageField(upload_to='logo/',blank=True,null=True)   
    price = models.IntegerField()
    old_price = models.IntegerField()
    rating = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)

   

    def __str__(self):   # Это возврошает по title не по id в админ
        return self.title


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'