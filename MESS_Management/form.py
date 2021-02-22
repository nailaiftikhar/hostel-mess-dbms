from django import forms
from django.forms import inlineformset_factory,HiddenInput
from django.db import models
from .models import MessAttendance

""" class AttendanceForm(forms.ModelForm):
    class Meta:
        model=MessAttendance
        widgets = {'student' : HiddenInput}
        fields=('att_date','att_time','status','menu','student') """
# AttendanceFormset = inlineformset_factory(MessAttendance,form=AttendanceForm,fields=(

attendance_choices = (
    ('present', 'P'),
    ('absent', 'A')
)
messtime_choices = (
    ('Lunch', 'lunch'),
    ('Dinner', 'dinner')
)

class messdate(forms.Form):
    mess_date= forms.CharField(required=True)
    mess_time = forms.ChoiceField(widget=forms.RadioSelect, choices=messtime_choices)

class AttendanceForm(forms.Form):
    mark_attendance = forms.ChoiceField(label='',widget=forms.RadioSelect,choices=attendance_choices)
    
