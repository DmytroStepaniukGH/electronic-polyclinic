from django.db import models


class Doctor(models.Model):
    name = models.CharField(verbose_name='ПІБ', max_length=300)
    specialization = models.CharField(verbose_name='Спеціалізація', max_length=150)
    price = models.IntegerField(verbose_name='Вартість прийому')
    info = models.CharField(verbose_name='Інформація про лікаря', max_length=1000)
    email = models.EmailField(verbose_name='Електронна адреса')

    def __str__(self):
        return f'{self.name} - {self.specialization}'
