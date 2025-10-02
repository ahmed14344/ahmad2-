from django.contrib import admin
from django.urls import path, include   # إضافة include لربط التطبيقات

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # روابط التطبيقات
    path('clients/', include('Clients.urls')),   # تطبيق العملاء
    path('fleet/', include('Fleet.urls')),       # تطبيق السيارات
    path('booking/', include('Booking.urls')),   # تطبيق الحجوزات
]
