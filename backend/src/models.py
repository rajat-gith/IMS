from tokenize import blank_re
from django.db import models


status=(
    ("A",'Active'),
    ("B","Inactive")
)    

colors=(
    ('Blue','Blue'),
    ('Black','Black'),
    ('Red','Red'),
    ('White','White'),
    ('Green','Green'),
    ('Yellow','Yellow'),
    ('Purple','purple')
)

categorys=(
    ('Men','Men'),
    ('Women','Women'),
    ('Child','Child'),
    ('Unisex','Unisex')
)
sexs=(
    ('Male',"Male"),
    ("Female","Female")
)

# Create your models here.
class Product_brand(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    quantity=models.IntegerField(blank=True)
    status=models.CharField(max_length=200,null=True,blank=True,choices=status)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return (self.name)

class product(models.Model):
    product_name=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    brand=models.ForeignKey(Product_brand,on_delete=models.CASCADE,null=True,blank=True,default="2")
    color=models.CharField(max_length=200,choices=colors,blank=True)
    category=models.CharField(max_length=200,choices=categorys,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    _id=models.AutoField(primary_key=True,editable=False)


    def __str__(self):
        return (self.product_name)

class store_owner(models.Model):
    owner_name=models.CharField(max_length=200,blank=True,null=True)
    store_count=models.IntegerField(blank=True)
    sex=models.CharField(choices=sexs,blank=True,null=True,max_length=200)
    owner_status=models.CharField(max_length=200,null=True,blank=True,choices=status)
    _id=models.AutoField(primary_key=True,editable=False)
    # store_list=models.ManyToManyField(stores)

    def __str__(self):
        return (self.owner_name)

class stores(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    brands=models.ManyToManyField(Product_brand)
    owner=models.ForeignKey(store_owner,on_delete=models.SET_NULL,null=True,blank=True)
    # outlets=models.IntegerField(blank=True)
    tagline=models.CharField(max_length=200,null=True,blank=True)
    status=models.CharField(max_length=200,null=True,blank=True,choices=status)
    _id=models.AutoField(primary_key=True,editable=False)

    def __str__(self):
        return (self.name)

class sales(models.Model):
    destination_store=models.ForeignKey(stores,on_delete=models.SET_NULL,null=True,related_name="Destination_Store")
    depart_store=models.ForeignKey(stores,on_delete=models.SET_NULL,null=True,related_name="Departed_Store")
    date_of_dispatch=models.DateTimeField(blank=True,null=True)
    quantity_shipment=models.IntegerField(blank=True,null=True)
    _id=models.AutoField(primary_key=True,editable=False)

    def __int__(self):
        return (self._id)

    
