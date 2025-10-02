from django.db import models

class Car(models.Model):
    الموديل = models.CharField(max_length=100)
    رقم_اللوحة = models.CharField(max_length=20, unique=True)
    متاح = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.الموديل} - {self.رقم_اللوحة}"
