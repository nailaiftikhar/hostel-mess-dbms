from django.shortcuts import render,redirect
#from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect, render, get_object_or_404, render
from django.contrib import messages
from django.views.generic import CreateView
from .forms import StudentSignUpForm, EmployeeSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User,Student,Mess_Employee,Feedback
from django.core import validators
from django.forms import CharField
from django import forms
from django.contrib.auth.decorators import login_required
from .decorators import student_required,employee_required

# Create your views here.

class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = '../templates/student_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

    def unique_user(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('username already exists.')
        return redirect('student_register')

class employee_register(CreateView):
    model = User
    form_class = EmployeeSignUpForm
    template_name = '../templates/employee_register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

    def unique_user(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('username already exists.')
        return redirect('employee_register')

def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/login.html',
    context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def feedback(request):

    if request.method == 'POST':

        Regnum = request.POST['Regnum']
        rating = request.POST['rating']
        date = request.POST['date']
        time = request.POST['time']
        Message = request.POST['Message']

       
        if Student.objects.filter(Regnum=Regnum).exists():
            feed = Feedback(Regnum=Regnum,rating=rating,Message=Message,time=time,date=date)
            feed.save()
            messages.info(request,'Feedback is recorded!')
            return redirect('feedback')   
        else:
            messages.info(request,'Registration number does not exist')
            return redirect('feedback')       
    else:
        return render(request,'feedback.html')

@login_required
def displayfeedbacks(request):
    info = Feedback.objects.all()
    feeddata = {"detail" : info}
    return render(request,'displayfeedbacks.html', context=feeddata) 

@login_required  
def displaystudentlist(request):
    info = Student.objects.all()
    employees = Mess_Employee.objects.select_related('user').values('user__first_name','user__last_name','Phone','designation','Salary')
    data = {"students":info,"employees":employees}
    return render(request,'listofstudents.html', context=data)