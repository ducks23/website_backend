from django.db import models
from django.contrib.auth.models import User, Permission

"""
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.CharField(max_length=100)
    subscription_valid = models.BooleanField(default=False)
    password = models.CharField(max_length=24)
    email = models.CharField(max_length=100)


class Subscription(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    subscribed = models.BooleanField(default=False)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
"""
