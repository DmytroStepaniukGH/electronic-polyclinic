from datetime import datetime, timedelta, time

from django.db import models
from django.utils import timezone

from accounts.models import User

TIME_CHOICES = (
    ("09:00", "09:00"),
    ("09:30", "09:30"),
    ("10:00", "10:00"),
    ("10:30", "10:30"),
    ("11:00", "11:00"),
    ("11:30", "11:30"),
    ("12:00", "12:00"),
    ("12:30", "12:30"),
    ("13:00", "13:00"),
    ("13:30", "13:30"),
    ("14:00", "14:00"),
    ("14:30", "14:30"),
    ("15:00", "15:00"),
    ("15:30", "15:30"),
    ("16:00", "16:00"),
    ("16:30", "16:30"),
    ("17:00", "17:00"),
    ("17:30", "17:30"),
)

STATUS_CHOICES = (
    ("Активний", "Активний"),
    ("Завершений", "Завершений"),
    ("Скасований", "Скасований"),
)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.patronim_name}'



class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='doctors_profile_images', default="default_image.png", blank=True)
    specialization = models.CharField(verbose_name='Спеціалізація', max_length=150)
    price = models.IntegerField(verbose_name='Вартість прийому')
    experience = models.CharField(verbose_name='Стаж', max_length=20)
    category = models.CharField(verbose_name='Категорія', max_length=30)
    info = models.CharField(verbose_name='Інформація про лікаря', max_length=1000)

    def get_available_slots(self, date):
        slots = [date, {}]

        for t in TIME_CHOICES:
            slots[1][t[0]] = True
        print(datetime.today().strftime('%Y-%m-%d %H:%M'))
        all_appointments = self.appointments.filter(day=date)
        for appointment in all_appointments:
            if appointment.time in slots[1].keys():
                slots[1][appointment.time] = False

        return slots

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}' \
               f' {self.user.patronim_name}. Email: {self.user.email}. ' \
               f'Спеціалізація: {self.specialization}'


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="09:00")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Активний")

    class Meta:
        unique_together = ('doctor', 'day', 'time')

    def __str__(self):
        return f'{self.patient} запис до {self.doctor} {self.day} о {self.time}'