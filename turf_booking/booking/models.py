from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    booking_date = models.DateField()
    time_slot = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.booking_date} - {self.time_slot}"
