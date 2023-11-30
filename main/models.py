from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    is_discount = models.BooleanField(default=False)