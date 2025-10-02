from django.db import models

class Client(models.Model):
    الاسم = models.CharField(max_length=100, verbose_name="الاسم")
    البريد_الإلكتروني = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    رقم_الجوال = models.CharField(max_length=15, verbose_name="رقم الجوال")

    class Meta:
        verbose_name = "عميل"
        verbose_name_plural = "العملاء"

    def __str__(self):
        return self.الاسم
