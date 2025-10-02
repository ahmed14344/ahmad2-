from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("الاسم", "البريد_الإلكتروني", "رقم_الجوال")   # الأعمدة في الجدول
    search_fields = ("الاسم", "البريد_الإلكتروني")               # البحث
