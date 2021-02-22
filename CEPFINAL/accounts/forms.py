from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Mess_Employee
from MESS_Management.models import BillRecord

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    Student_CNIC = forms.CharField(required=True)
    Regnum = forms.CharField(required=True)
    Gender = forms.CharField(required=True)
    Room_No = forms.IntegerField(required=True)
    Email= forms.CharField(required=True)
    Department_Name = forms.CharField(required=True)
    Father_Name = forms.CharField(required=True)
    Father_CNIC = forms.CharField(required=True)
    Phone_No = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('Email')
        user.save()
        student = Student.objects.create(user=user)
        student.Student_CNIC=self.cleaned_data.get('Student_CNIC')
        student.Regnum=self.cleaned_data.get('Regnum')
        student.Room_No=self.cleaned_data.get('Room_No')
        student.Email=self.cleaned_data.get('Email')
        student.Father_Name=self.cleaned_data.get('Father_Name')
        student.Father_CNIC=self.cleaned_data.get('Father_CNIC')
        student.Phone_No=self.cleaned_data.get('Phone_No')
        student.Gender=self.cleaned_data.get('Gender')
        student.Department_Name=self.cleaned_data.get('Department_Name')
        student.save()
        BillRecord.objects.create(student=student)
        return user

class EmployeeSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    designation = forms.CharField(required=True)
    Phone = forms.CharField(required=True)
    Salary = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        employee = Mess_Employee.objects.create(user=user)
        employee.Phone=self.cleaned_data.get('Phone')
        employee.designation=self.cleaned_data.get('designation')
        employee.Salary=self.cleaned_data.get('Salary')
        employee.save()
        return user

