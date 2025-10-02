from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("العميل", "السيارة", "تاريخ_البدء", "تاريخ_الانتهاء", "تم_الدفع")
    list_filter = ("تم_الدفع", "تاريخ_البدء")
    search_fields = ("العميل__الاسم", "السيارة__الموديل")
