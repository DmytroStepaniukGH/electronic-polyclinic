# Generated by Django 4.1.7 on 2023-04-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_doctor_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Активний', 'Активний'), ('Завершений', 'Завершений'), ('Скасований', 'Скасований')], default='Активний', max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='profile_image',
            field=models.ImageField(blank=True, default='default_image.png', upload_to=''),
        ),
    ]