from rest_framework import serializers
from .models import Appointment, Doctor


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorListSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')
    patronim_name = serializers.CharField(source='user.patronim_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'email',
            'profile_image',
            'last_name',
            'first_name',
            'patronim_name',
            'specialization',
            'price',
            'category',
            'experience',
            'info',
        )


class SpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('specialization',)


class SearchSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'last_name',
            'specialization'
        )
