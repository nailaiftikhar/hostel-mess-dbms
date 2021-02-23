from django.db import models
from datetime import datetime
from accounts.models import User,Student,Mess_Employee

# Create your models here.
messtime_choices = (
    ('Lunch', 'lunch'),
    ('Dinner', 'dinner')
)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    day = models.CharField(max_length=30)
    desc = models.TextField(null=True)
    Price = models.IntegerField(null=True)
    time = models.CharField(max_length=8, choices=messtime_choices, blank=True)
    

attendance_choices = (
    ('absent', 'A'),
    ('present', 'P')
)

class AttendanceManager(models.Manager):
    def create_attendance(self,student_reg,std_id,date,day,time):
        student_obj = Student.objects.get(Regnum=student_reg)
        menu_obj = Menu.objects.get(day=day, time=time)
        attendance_obj = MessAttendance.objects.create(student=student_obj,menu=menu_obj, status=std_id,att_date=date,att_day=day,att_time=time)
        return attendance_obj
    def menu_attendance(self, time, date):
        std_att = MessAttendance.objects.filter(att_time= time, att_date=date)   
        return std_att

class MessAttendance(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    menu = models.ForeignKey('Menu', on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=8, choices=attendance_choices, blank=True)
    att_date = models.CharField(max_length=100)
    att_day = models.CharField(max_length=30, blank=True)
    att_time = models.CharField(max_length=8, choices=messtime_choices, blank=True)

    objects = AttendanceManager()


class BillRecord(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    bill = models.IntegerField(default=350)
    def __str__(self):
        return self.bill   

