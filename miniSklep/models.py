from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()

class Users(models.Model):
    login = models.CharField(max_length=64)
    passw = models.CharField(max_length=64)