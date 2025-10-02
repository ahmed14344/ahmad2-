from django.db import models

class Car(models.Model):
    الموديل = models.CharField(max_length=100, verbose_name="الموديل")
    رقم_اللوحة = models.CharField(max_length=20, unique=True, verbose_name="رقم اللوحة")
    متاح = models.BooleanField(default=True, verbose_name="متاح")

    class Meta:
        verbose_name = "سيارة"
        verbose_name_plural = "السيارات"

    def __str__(self):
        return f"{self.الموديل} - {self.رقم_اللوحة}"
