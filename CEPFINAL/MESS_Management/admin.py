from django.contrib import admin
from .models import Menu, AttendanceManager, MessAttendance, BillRecord
# Register your models here.

admin.site.register(Menu)
admin.site.register(MessAttendance)
admin.site.register(BillRecord)
