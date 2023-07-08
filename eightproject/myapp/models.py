from django.db import models
from datetime import datetime

# Create your models here.

class Booking(models.Model):

    name = models.CharField(max_length=255)
    guest_quantity = models.IntegerField()
    date = models.DateTimeField(default=datetime.now, blank=True)


class Menu(models.Model):

    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
            return 'id: '+ str(self.pk) +', ' + self.title

