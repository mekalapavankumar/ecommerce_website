from django.db import models

# Create your models here.

class Category(models.Model):
    catid = models.IntegerField(primary_key=True)
    catname = models.CharField(max_length=20)

    def __str__(self):
        return self.catname

class Product(models.Model):
    prdid = models.IntegerField(primary_key=True)
    prdname = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',null=True)