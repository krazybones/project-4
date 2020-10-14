from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # pass account balance and transaction history here? i.e:
    # balance = models.IntegerField()

    def __str__(self):
        return 'self.user.username Profile'


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
