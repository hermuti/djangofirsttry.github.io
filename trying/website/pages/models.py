from sre_constants import CATEGORY
from typing import Any
from django.db import models

# Create your models here.

#company info
#products


class CompanyInformation(models.Model):
  name= models.CharField(max_length=100)
  description = models.TextField()

class category(models.Model):
  name= models.CharField(max_length=100)
  

class Product(models.Model):
  product_name=models.CharField(max_length=100)
  product_description = models.TextField()
  category =models.ForeignKey(category, on_delete=models.CASCADE)
   


