from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema

from django.db.models import Avg, Count, Sum, Value
from rest_framework import generics, status, viewsets, filters
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, Doctor
from reviews.models import Review # noqa
from .serializers import AppointmentSerializer, DoctorListSerializer, SpecializationsSerializer, SearchSerializer


@extend_schema(
    tags=['Appointments']
)
class AppointmentCreateView(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@extend_schema(
    tags=['Appointments'],
    description="Return list of appointments for authorized user"
)
class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.is_doctor:
            return super().get_queryset().filter(doctor_id=self.request.user.doctor)

        return super().get_queryset().filter(patient_id=self.request.user.patient)


@extend_schema(
    tags=['Appointments']
)
class AvailableSlotsView(APIView):
    def get(self, *args, **kwargs):
        doctor_id = self.request.parser_context.get('kwargs')['doctor_id']
        date_str = self.request.parser_context.get('kwargs')['date']
        if not doctor_id or not date_str:
            return Response({'Error': 'Doctor ID and date are required.'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            doctor = Doctor.objects.get(id=doctor_id)

        except Doctor.DoesNotExist:
            return Response({'Error': f'Doctor with ID {doctor_id} does not exist.'}, status=status.HTTP_404_NOT_FOUND)

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

        except ValueError:
            return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        available_slots = doctor.get_available_slots(date)

        return Response(available_slots, status=status.HTTP_200_OK)


@extend_schema(
    tags=['Doctors']
)
class SearchAPIView(generics.ListAPIView):
    search_fields = ['user__last_name', 'specialization']
    filter_backends = (filters.SearchFilter,)
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer


@extend_schema(
    tags=['Doctors']
)
class AllSpecializations(APIView):

    def get(self, request):
        return Response(Doctor.objects.values_list("specialization").distinct(), status=status.HTTP_200_OK)


@extend_schema(
    tags=['Doctors']
)
class DoctorsListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()

        return queryset


@extend_schema(
    tags=['Doctors'],
    description="Return information about doctor"
)
class DoctorView(APIView):
    serializer_class = DoctorListSerializer

    def get(self, *args, **kwargs):
        doctor_id = self.request.parser_context.get('kwargs')['doctor_id']

        doctor_info = Doctor.objects.get(id=doctor_id)
        doctor_serializer = DoctorListSerializer(doctor_info)

        return Response(doctor_serializer.data, status=status.HTTP_200_OK)


@extend_schema(
    tags=['Doctors'],
    description="Return list of all doctors if parameter 'specialization' not provided."
                "Else return list of doctors filtered by specialization"

)
class FilterDoctors(viewsets.ReadOnlyModelViewSet):
    model = Doctor
    serializer_class = DoctorListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Doctor.objects.all()
        specialization = self.request.parser_context.get('kwargs')['specialization']

        if specialization:
            queryset = queryset.filter(specialization=specialization)

        return queryset



