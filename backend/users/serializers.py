from rest_framework import serializers
from .models import Appointment, Doctor, DoctorUnavailableTime
from reviews.models import Review # noqa


class AppointmentSerializer(serializers.ModelSerializer):
    #patient_last_name = serializers.CharField(source='patient.user.last_name')
    #date = serializers.DateField()

    class Meta:
        model = Appointment
        fields = (
            'id',
            'date',
            'time',
            'patient',
            'doctor',
            'status',
            'medical_history',
            'objective_status',
            'diagnosis',
            'examination',
            'recommendations'
        )

    # def create(self, validated_data):
    #     return Appointment.objects.create(**validated_data)


class DoctorListSerializer(serializers.ModelSerializer):
    last_name = serializers.CharField(source='user.last_name')
    first_name = serializers.CharField(source='user.first_name')
    patronim_name = serializers.CharField(source='user.patronim_name')
    email = serializers.CharField(source='user.email')
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