# Generated by Django 4.1.7 on 2023-04-02 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_confirmed',
            field=models.BooleanField(blank=True, default=0, verbose_name='Верифікований'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_appartment',
            field=models.CharField(blank=True, max_length=10, verbose_name='Квартира'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_city',
            field=models.CharField(blank=True, max_length=50, verbose_name='Місто'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_house',
            field=models.CharField(blank=True, max_length=10, verbose_name='Будинок'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address_street',
            field=models.CharField(blank=True, max_length=150, verbose_name='Вулиця'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.CharField(blank=True, max_length=8, verbose_name='Дата народження'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Імʼя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Прізвище'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patronim_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='По-батькові'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_num',
            field=models.CharField(blank=True, max_length=13, verbose_name='Номер телефону'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, max_length=10, verbose_name='Стать'),
        ),
    ]
