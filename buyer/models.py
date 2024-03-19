from django.db import models
from seller.models import *
class Buyer_tb(models.Model):
    Name = models.CharField(max_length =20)
    Gender = models.CharField(max_length =20)
    Age = models.CharField(max_length =20)
    Addresss= models.CharField(max_length =20)
    Place = models.CharField(max_length =20)
    Phone = models.CharField(max_length =20)
    username = models.CharField(max_length =20)
    password = models.CharField(max_length =20)
class cart_tb(models.Model):
    Product_id = models.ForeignKey(product_tb,on_delete=models.CASCADE)
    Buyer_id =models.ForeignKey(Buyer_tb,on_delete = models.CASCADE)
    Quantity = models.IntegerField()
    Total = models.IntegerField()
class order_tb(models.Model):
    Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Buyer_id = models.ForeignKey(Buyer_tb,on_delete=models.CASCADE)
    Orderdate = models.CharField(max_length = 20)
    Ordertime = models.CharField(max_length =20)
    Status = models.CharField(max_length = 20,default="pending")
    Grandtotal = models.IntegerField()
class orderItems_tb(models.Model):
    Order_Id = models.ForeignKey(order_tb,on_delete=models.CASCADE)
    Product_id = models.ForeignKey(product_tb,on_delete=models.CASCADE)
    Buyer_id = models.ForeignKey(Buyer_tb,on_delete=models.CASCADE) 
    Quantity = models.IntegerField()
    Price = models.IntegerField()
class payment_tb(models.Model):
    Buyer_id = models.ForeignKey(Buyer_tb,on_delete=models.CASCADE)
    order_id = models.ForeignKey(order_tb,on_delete=models.CASCADE)
    Name_on_card = models.CharField(max_length=20)
    Card_number = models.IntegerField()
    Expiry_date = models.CharField(max_length=20)
    Cvv = models.IntegerField()
# Create your models here.
