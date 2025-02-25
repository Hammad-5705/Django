from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id=models.AutoField
    Product_Name=models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    Product_Disc=models.CharField(max_length=400)
    Publish_Date=models.DateField()
    image=models.ImageField(upload_to="Alpino_Store/images",default="")

    def __str__(self):
        return self.Product_Name
