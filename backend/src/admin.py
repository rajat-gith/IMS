from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(store_owner)
admin.site.register(brand)
admin.site.register(stores)
admin.site.register(product)
admin.site.register(sales)