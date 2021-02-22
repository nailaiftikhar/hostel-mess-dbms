# Generated by Django 3.1.4 on 2021-02-22 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.IntegerField(default=350)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=30)),
                ('desc', models.TextField(null=True)),
                ('Price', models.IntegerField(null=True)),
                ('time', models.CharField(blank=True, choices=[('Lunch', 'lunch'), ('Dinner', 'dinner')], max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='MessAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('absent', 'A'), ('present', 'P')], max_length=8)),
                ('att_date', models.CharField(max_length=100)),
                ('att_day', models.CharField(blank=True, max_length=30)),
                ('att_time', models.CharField(blank=True, choices=[('Lunch', 'lunch'), ('Dinner', 'dinner')], max_length=8)),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MESS_Management.menu')),
            ],
        ),
    ]