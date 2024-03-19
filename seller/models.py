from django.db import models
from site_admin.models import *
from buyer.models import *
class seller_tb(models.Model):
    Name = models.CharField(max_length =20)
    Gender = models.CharField(max_length = 20)
    Age = models.CharField(max_length =20)
    Addresss= models.CharField(max_length =20)
    Place = models.CharField(max_length =20)
    Phone = models.CharField(max_length =20)
    username = models.CharField(max_length =20)
    password = models.CharField(max_length =20)
    image =  models.FileField()
    status = models.CharField(max_length =20, default = "pending")
class product_tb(models.Model):
    Name = models.CharField(max_length =20)
    Image = models.FileField()
    Price = models.IntegerField()
    Stock = models.IntegerField(default="none")
    Details = models.CharField(max_length=20,default="none")
    seller_id = models.ForeignKey(seller_tb,on_delete = models.CASCADE)
    category_id = models.ForeignKey(category_tb,on_delete = models.CASCADE)
class ordertracking_tb(models.Model):
    Order_id = models.ForeignKey('buyer.order_tb',on_delete=models.CASCADE)
    Details = models.CharField(max_length=20)
    Orderdate = models.CharField(max_length = 20)
    Ordertime = models.CharField(max_length =20)
# Create your models here.
