from django.db import models

class Client(models.Model):
    الاسم = models.CharField(max_length=100)
    البريد_الإلكتروني = models.EmailField(unique=True)
    رقم_الجوال = models.CharField(max_length=15)

    def __str__(self):
        return self.الاسم
