from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id=models.AutoField
    Product_Name=models.CharField(max_length=50)
    Product_Disc=models.CharField(max_length=400)
    Publish_Date=models.DateField()
