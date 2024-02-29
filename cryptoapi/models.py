from django.db import models

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=14, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
