from django.db import models


class Review(models.Model):
    appointment = models.OneToOneField(to='users.Appointment', on_delete=models.CASCADE, default=1)
    doctor = models.ForeignKey(to='users.Doctor', on_delete=models.CASCADE, default=1)
    review_rating = models.FloatField(default=0)
    review_text = models.CharField(max_length=2000)
