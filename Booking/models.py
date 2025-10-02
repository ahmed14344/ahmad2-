from django.db import models
from Clients.models import Client
from Fleet.models import Car

class Booking(models.Model):
    العميل = models.ForeignKey(Client, on_delete=models.CASCADE)
    السيارة = models.ForeignKey(Car, on_delete=models.CASCADE)
    تاريخ_البدء = models.DateTimeField()
    تاريخ_الانتهاء = models.DateTimeField()
    تم_الدفع = models.BooleanField(default=False)

    def __str__(self):
        return f"حجز {self.العميل} - {self.السيارة}"
