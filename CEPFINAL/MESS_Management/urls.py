from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('menu',views.menu, name='menu'),
    path('student_attendance',views.student_attendance, name='student_attendance'),
    path('view_attendance',views.view_attendance, name='view_attendance'),
    path('view_bill',views.view_bill, name='view_bill'),
]
