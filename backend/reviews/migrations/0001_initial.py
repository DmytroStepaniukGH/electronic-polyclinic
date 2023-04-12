# Generated by Django 4.1.7 on 2023-04-10 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0008_appointment_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.FloatField()),
                ('review_text', models.CharField(max_length=2000)),
                ('doctor', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('patient', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
        ),
    ]
