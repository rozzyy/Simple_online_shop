from django.db import models
from django.contrib.auth.models import AbstractUser
from products.models import Cart, Order

# Create your models here.
class Account(AbstractUser):
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return self.username
