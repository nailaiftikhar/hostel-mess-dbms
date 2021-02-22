from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.username

class Student(models.Model):
    Student_CNIC = models.CharField(max_length= 20)
    Regnum = models.TextField(max_length=13)
    Gender = models.CharField(max_length= 10)
    Room_No = models.IntegerField(null=True)
    Email= models.CharField(max_length= 40)
    Department_Name = models.CharField(max_length= 30)
    Father_Name = models.CharField(max_length= 30)
    Father_CNIC = models.CharField(max_length= 20)
    Phone_No = models.CharField(max_length= 30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return self.Regnum
    
    # Create your models here.
class Mess_Employee(models.Model):
    Phone = models.CharField(max_length= 30)
    Salary = models.IntegerField(null=True)
    designation = models.CharField(max_length= 30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class hostel(models.Model):
    Hostel_Name = models.CharField(max_length= 30)
    Location = models.CharField(max_length= 30)
    Admin = models.ForeignKey(Mess_Employee, on_delete = models.CASCADE)


# Create your models here.
class Feedback(models.Model):
    Regnum = models.TextField(max_length=13)
    date = models.DateField(default='',blank=True, null=True)
    rating = models.IntegerField()
    time = models.CharField(max_length=20)
    Message = models.TextField()
    Student = models.ForeignKey(Student, blank=True, null=True,on_delete = models.CASCADE)

