from django.db import models
from users.models import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
