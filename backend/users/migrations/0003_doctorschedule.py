# Generated by Django 4.1.7 on 2023-03-29 12:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_appointment_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=datetime.datetime.now)),
                ('time', models.CharField(choices=[('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30')], default=(('09:00', '09:00'), ('09:30', '09:30'), ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'), ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30')), max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule', to='users.doctor')),
            ],
        ),
    ]
