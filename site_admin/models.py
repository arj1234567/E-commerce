from django.db import models
class admin_tb(models.Model):
    username = models.TextField(max_length = 20)
    password = models.TextField(max_length = 20)
class category_tb(models.Model):
    name = models.TextField(max_length =20)

# Create your models here.
