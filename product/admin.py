from django.contrib import admin
from .models import ProductsCategory,Products,Savat,coment,color, hearth, city

# Register your models here.
admin.site.register(Products)
admin.site.register(ProductsCategory)
admin.site.register(Savat)
admin.site.register(color)

admin.site.register(coment)
admin.site.register(hearth)
admin.site.register(city)





