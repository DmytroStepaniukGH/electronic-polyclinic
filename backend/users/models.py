from datetime import datetime
from django.db import models

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
    ("Active", "Active"),
    ("Closed", "Closed"),
)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} {self.user.patronim_name}'

    def create_appointment(self, doctor_id, date, time):
        check_another_appointment = Appointment.objects.filter(patient=self, date=date, time=time)

        if check_date_time(date, time):

            doctor = Doctor.objects.get(id=doctor_id)

            unavailable_times = doctor.unavailable_time.filter(date=date).values_list('time', flat=True)

            if not check_another_appointment:
                if time not in unavailable_times:
                    appointment = Appointment(patient=self, doctor=doctor, day=date, time=time)
                    appointment.save()
                    return f'Appointment at {date} {time} has been created successfully'
                else:
                    return f'Error: time {time} on {date} has been marked by doctor as unavailable'
            else:
                return f'Error: you already have another appointment at {time} on {date}'

        else:
            return 'Date/time not valid'

    '''
    def cancel_appointment(self, date, time):

        appointment = self.appointments.filter(day=date).filter(time=time)
        if appointment:
            appointment.status = 'Скасовано'
            print('Status', appointment.status)
            appointment.save(update_fields=['status'])
            print(appointment.status)

        else:
            return Exception('Не знайдено записів з такими датою і часом')
    '''


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(verbose_name='Фото профіля',
                                      upload_to='doctor_profile_photo',
                                      default="doctor_profile_photo/default_image.png",
                                      blank=True)

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

        all_appointments = self.appointments.filter(date=date)
        unavailable_times = self.unavailable_time.filter(date=date).values_list('time', flat=True)

        print(unavailable_times)

        for appointment in all_appointments:
            if appointment.time in slots[1].keys():
                slots[1][appointment.time] = False

        for time in slots[1].keys():
            if time in unavailable_times:
                slots[1][time] = False

        return slots

    def set_unavailable_time(self, date, time):
        unavailable_time = DoctorUnavailableTime(doctor=self, date=date, time=time)
        unavailable_time.save()


    def __str__(self):
        return f'{self.specialization} - {self.user.last_name} {self.user.first_name}' \
               f' {self.user.patronim_name}. Email: {self.user.email}. '


class DoctorUnavailableTime(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='unavailable_time')
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="09:00")


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="09:00")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="Active")

    medical_history = models.CharField(verbose_name='Анамнез захворювання',
                                       default='', blank=True, max_length=1000)
    objective_status = models.CharField(verbose_name="Об'єктивний статус",
                                        default='', blank=True, max_length=1000)
    diagnosis = models.CharField(verbose_name='Діагноз',
                                        default='', blank=True, max_length=500)
    examination = models.CharField(verbose_name='Обстеження',
                                        default='', blank=True, max_length=1000)
    recommendations = models.CharField(verbose_name='Рекомендації',
                                        default='', blank=True, max_length=1000)

    class Meta:
        unique_together = ('doctor', 'date', 'time')

    def __str__(self):
        return f'{self.patient} запис до {self.doctor} {self.date} о {self.time}'


def check_date_time(date, time):
    today = datetime.today().strftime('%Y-%m-%d')
    time_now = datetime.now().strftime('%H:%M')

    if date > today:
        if time in (time, time) in TIME_CHOICES:
            return True
        else:
            return False

    elif date == today:
        if time >= time_now and (time, time) in TIME_CHOICES:
            return True
        else:
            return False

    else:
        return False
