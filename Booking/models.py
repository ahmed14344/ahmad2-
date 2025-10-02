from django.db import models
from Clients.models import Client
from Fleet.models import Car

class Booking(models.Model):
    العميل = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="العميل")
    السيارة = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name="السيارة")
    تاريخ_البدء = models.DateTimeField(verbose_name="تاريخ البدء")
    تاريخ_الانتهاء = models.DateTimeField(verbose_name="تاريخ الانتهاء")
    تم_الدفع = models.BooleanField(default=False, verbose_name="تم الدفع")

    class Meta:
        verbose_name = "حجز"
        verbose_name_plural = "الحجوزات"

    def __str__(self):
        return f"حجز {self.العميل} - {self.السيارة}"
