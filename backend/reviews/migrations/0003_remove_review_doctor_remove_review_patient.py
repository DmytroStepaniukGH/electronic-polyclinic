# Generated by Django 4.1.7 on 2023-04-10 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_appointment_alter_review_doctor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='review',
            name='patient',
        ),
    ]
