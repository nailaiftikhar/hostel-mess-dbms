from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404,HttpResponseRedirect
from django.contrib import messages
from .form import messdate,AttendanceForm
from .models import MessAttendance,Menu,BillRecord
from accounts.models import Student
from django.contrib.auth.forms import AuthenticationForm
from django.core import validators
from django import forms
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required,employee_required
from django.forms.formsets import formset_factory
from django.db.models import Sum

#from .models import Destination

# Create your views here.

def index(request):
    return render(request,'index.html')

def menu(request):
    Lmenu = Menu.objects.filter(time='Lunch')
    Dmenu = Menu.objects.filter(time='Dinner')
    return render(request,'menu.html',context={'Lmenu':Lmenu,'Dmenu':Dmenu})

def student_attendance(request):
    students = Student.objects.all()
    count = students.count()
    attendance_formset = formset_factory(AttendanceForm, extra=count)
    
    if request.method == 'POST':
        mess_date = request.POST['mess_date']
        day =  request.POST['mess_day']
        time =  request.POST['mess_time']
        formset = attendance_formset(request.POST or None)
        if formset.is_valid():
            for student,form in zip(students,formset):
                mark = form.cleaned_data['mark_attendance']
                MessAttendance.objects.create_attendance(student.Regnum,mark, mess_date,day,time)
            messages.info(request,'Attendance is recorded!')
            return redirect('student_attendance')  
    else:
        formset = attendance_formset()
    mylist = zip(students,formset)
    return render(request,'student_attendance.html',context = {'formset':formset,'mylist':mylist})
    
# Create your views here.
""" @employee_required
def attendance_form(request):

    def create_attendance(student_id,date,time):
        student_obj = Student.objects.get(
            Regnum=student_id
        )
        menu_obj = Menu.objects.get(date=date, time=time)
        attendance_obj = MessAttendance.objects.create(student=student_obj,menu=menu_obj, status='Present',att_date=menu_obj.date,att_time=menu_obj.time)
        return attendance_obj
        
    if request.method == 'POST':
        Menu_date = request.POST['Menu_date']
        Menu_time = request.POST['Menu_time']
        Reg_Num = request.POST['Reg_Num']
        #student_obj = Student.objects.get(Regnum=Reg_Num)
        if Menu.objects.filter(date=Menu_date,time=Menu_time).exists():
            create_attendance(Reg_Num,Menu_date,Menu_time)
            menu_ob= Menu.objects.filter(date=Menu_date,time=Menu_time)
            rec=BillRecord.objects.create(student=student_obj,bill=menu_ob)
            return redirect('attendance_form')   
        else:
            messages.info(request,'No menu exists for the entered date')
            return redirect('attendance_form')       
    else:
        return render(request,'attendance_form.html') """

""" def attendance_form(request):
    student_list = Student.objects.all()
    context = {"student_list": student_list}
    def create_attendance(student_id,date,time):
        student_obj = Student.objects.get(
            Regnum=student_id
        )
        menu_obj = Menu.objects.get(date=date, time=time)
        attendance_obj = MessAttendance.objects.create(student=student_obj,menu=menu_obj, status='Present',att_date=menu_obj.date,att_time=menu_obj.time)
        return attendance_obj
    if request.method == 'POST':    
        mess_date = request.POST.get('mess_date',False)
        mess_time = request.POST.get('mess_time',False)
        att_list = request.POST.getlist('att_list')
        for id in att_list:
            global att
            att = get_object_or_404(att, code=id)
            create_attendance(att,mess_date,mess_time)
            return redirect('/') 
    else:
        return render(request,'attendance_form.html', context)

""" 
def view_attendance(request):
    if request.method == 'POST':
        Att_date = request.POST.get('Att_date',False)
        Att_time = request.POST.get('Att_time',False)
        if MessAttendance.objects.filter(att_date=Att_date,att_time=Att_time).exists():
            mess=MessAttendance.objects.filter(att_date=Att_date,att_time=Att_time)
            return render(request,'attendance_list.html',context={'mess':mess,'Att_date':Att_date,'Att_time':Att_time})  
        else:
            messages.info(request,'No attendance for the entered date')
            return redirect('view_attendance')     
    else:
        return render(request,'view_attendance.html')

def view_bill(request):
    if request.method == 'POST':
        Reg_Num = request.POST.get('Reg_Num',False)
        std_id = Student.objects.get(Regnum=Reg_Num)
        bill = MessAttendance.objects.filter(student=std_id,status='present' or 'P').select_related('menu').values('menu__Price').aggregate(Sum('menu__Price'))['menu__Price__sum']
        return render(request,'show_bill.html',context={'Reg_Num':Reg_Num,'bill':bill})  
    else:
         return render(request,'view_bill.html')      