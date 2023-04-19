from rest_framework import serializers
from .models import Appointment, Doctor, DoctorUnavailableTime, Specialization
from reviews.models import Review # noqa


class AppointmentSerializer(serializers.ModelSerializer):
    #patient_last_name = serializers.CharField(source='patient.user.last_name')
    #date = serializers.DateField()
    doctor_lastname = serializers.CharField(source='doctor.user.last_name')
    doctor_name = serializers.CharField(source='doctor.user.first_name')
    doctor_patronim = serializers.CharField(source='doctor.user.patronim_name')
    specialization = serializers.CharField(source='doctor.specialization.name')

    class Meta:
        model = Appointment
        fields = (
            'id',
            'date',
            'time',
            'patient',
            'doctor',
            'doctor_lastname',
            'doctor_name',
            'doctor_patronim',
            'specialization',
            'status',
            'medical_history',
            'objective_status',
            'diagnosis',
            'examination',
            'recommendations'
        )


class DoctorListSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')
    patronim_name = serializers.CharField(source='user.patronim_name')
    email = serializers.CharField(source='user.email')
    specialization = serializers.CharField(source='specialization.name')
    rating = serializers.SerializerMethodField('get_average_rating')

    def get_average_rating(self, obj):
        reviews_rating = Review.objects.filter(doctor_id=obj.id).values_list('review_rating', flat=True)
        rating_avg = 0
        if reviews_rating:
            rating_avg = round(sum(reviews_rating) / len(reviews_rating), 2)
        return rating_avg

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
            'rating',
        )


class SpecializationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = ('name', 'image')


class SearchSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')
    specialization = serializers.CharField(source='doctor.specialization.name')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'last_name',
            'specialization'
        )


class SetUnavailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorUnavailableTime
        fields = (
            'id',
            'doctor',
            'date',
            'time',
        )


class CreateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'doctor',
            'date',
            'time',
        )