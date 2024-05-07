from django.core.validators import MaxValueValidator, MinValueValidator


from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ProductsCategory(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "ProductsCategory"
class color(models.Model):
    rang = models.CharField(max_length=100)
    def __str__(self):
        return self.rang
    
    class Meta:
        verbose_name_plural = "Rang"
class Products(models.Model):
    userr = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=ProductsCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_images')
    old_prices = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.IntegerField()
    rang1 = models.ForeignKey(color, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural = "Products"
    
    def __str__(self):
        return f"Mahsulot: {self.name} | Kategoriya: {self.category.name}"
    
class Savat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    creates_timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Xaridor: {self.user.first_name} | Mahsulot { self.product.name }"
class coment(models.Model):
    rate = models.PositiveBigIntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ])
    time = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='comment')
    pro = models.ForeignKey(Products, on_delete=models.CASCADE)
    userr = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()

    
class hearth(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

class city(models.Model):
    dshahar = models.CharField(max_length=200)
    def __str__(self):

        return self.dshahar
class shahar(models.Model):
    shahar_fd = models.ForeignKey(city,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.shahar_fd