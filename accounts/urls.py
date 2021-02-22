from django.urls import include, path

from . import views

urlpatterns=[
     path('student_register/',views.student_register.as_view(), name='student_register'),
     path('employee_register/',views.employee_register.as_view(), name='employee_register'),
     path('login/',views.login_request, name='login'),
     path('logout/',views.logout_view, name='logout'),
     path('feedback',views.feedback, name='feedback'),
     path('displayfeedbacks',views.displayfeedbacks, name='displayfeedbacks'),
     path('listofstudents',views.displaystudentlist, name='displaystudentlist')
]
