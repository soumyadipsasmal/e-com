from django.contrib import admin
from .models import Category,Sub_Category
from .models import Products
from .models import ContactUs
from .models import Order
from .models import Brand


# Register your models here.
admin.site.register(Category )
admin.site.register(Sub_Category)
admin.site.register(Products)
admin.site.register(ContactUs)
admin.site.register(Order)
admin.site.register(Brand)


 