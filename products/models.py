from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    product_id = models.CharField(max_length=12)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    date_release = models.DateTimeField(auto_now_add=False)
    stock = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    
    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    rating = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ManyToManyField(Cart)
    ordered = models.BooleanField(default=False)
    date_ordered = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)

    def __str__(self):
        return f"order of self.user.username"
