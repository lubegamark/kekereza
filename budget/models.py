from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Income(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    description = models.TextField()


class Expense(models.Model):
    user = models.ForeignKey(User)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    description = models.TextField()