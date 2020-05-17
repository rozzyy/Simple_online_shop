from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Cart, Order

# Create your models here.
class Account(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    about = models.TextField()
    cart = models.ManyToManyField(Cart)
    ordered = models.ManyToManyField(Order)
    image = models.ImageField(upload_to='images/users/')
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"self.user.first_name self.user.last_name"