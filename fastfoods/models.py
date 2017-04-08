from __future__ import unicode_literals

from django.db import models
from djmoney.models.fields import MoneyField

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True, db_index=True)
    category_name = models.CharField(max_length=100)
    # list_display = (category_id,category_name)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True, db_index=True)
    product_name = models.CharField(max_length=100)
    product_price = MoneyField(decimal_places=2, default=0, default_currency='INR', max_digits=12)
    product_description = models.TextField()
    product_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='uploads/')
    # list_display = (product_id,product_name,product_price,product_description,product_cat,product_image)

    def __str__(self):
        return self.product_name
class UserComments(models.Model):
    Choices=[('ACTIVE','active'),('DISABLED','disabled')]
    user_email=models.EmailField()
    user_name=models.CharField(max_length=100)
    user_message=models.TextField()
    active_or_disable=models.CharField(max_length=15,choices=Choices,default='DISABLED',blank=True,null=True)

    


