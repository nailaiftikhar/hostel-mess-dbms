from django.contrib import admin

# Register your models here.
from .models import User, Student, Mess_Employee,hostel, Feedback

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Mess_Employee)
admin.site.register(hostel)
admin.site.register(Feedback)
