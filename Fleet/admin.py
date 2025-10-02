from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("الموديل", "رقم_اللوحة", "متاح")
    list_filter = ("متاح",)         # فلترة حسب التوفر
    search_fields = ("الموديل", "رقم_اللوحة")
