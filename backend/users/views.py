from datetime import datetime, timedelta

from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, viewsets, filters
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Appointment, Doctor, Patient
from .serializers import AppointmentSerializer, DoctorListSerializer, SpecializationsSerializer, SearchSerializer


@extend_schema(
    tags=['Appointments']
)
class CreateAppointmentView(APIView):

    def post(self, request, *args, **kwargs):
        date = self.request.parser_context.get('kwargs')['date']
        time = self.request.parser_context.get('kwargs')['time']
        doctor_id = self.request.parser_context.get('kwargs')['doctor_id']

        patient = Patient.objects.get(user=self.request.user)
        doctor = Doctor.objects.get(id=doctor_id)

        check_another_appointment = Appointment.objects.filter(patient=patient, day=date, time=time)

        if not check_another_appointment:
            appointment = Appointment(patient=patient, doctor=doctor, day=date, time=time)
            appointment.save()
            return Response(f'Appointment at {date} {time} has been created successfully',
                            status=status.HTTP_200_OK)
        else:
            return Response(f'Error. Exist another appointment at {date} {time}', status=status.HTTP_400_BAD_REQUEST)


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
    tags=['Appointments']
)
class CancelAppointmentView(APIView):

    def post(self, *args, **kwargs):
        date_to_cancel = self.request.parser_context.get('kwargs')['date']
        time_to_cancel = self.request.parser_context.get('kwargs')['time']

        if not date_to_cancel or not time_to_cancel:
            return Response({'Error': 'Date and time are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_to_cancel = datetime.strptime(date_to_cancel, '%Y-%m-%d').date()

        except ValueError:
            return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(user=self.request.user)

        except Patient.DoesNotExist:
            return Response({'Error': f'Cancel appointment can only authorized patient'}, status=status.HTTP_404_NOT_FOUND)

        appointment = Appointment.objects.get(patient=patient, day=date_to_cancel, time=time_to_cancel)
        print('Статус', appointment.status)
        if appointment:
            appointment.status = 'Скасовано'
            #appointment.save()
            appointment.delete()
            return Response(f'Appointment canceled', status=status.HTTP_200_OK)
        else:
            return Response(f'Error', status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    tags=['Doctors']
)
class SetUnavailableTimeView(APIView):

    def post(self, *args, **kwargs):
        date_to_set_unavailable = self.request.parser_context.get('kwargs')['date']
        time_to_set_unavailable = self.request.parser_context.get('kwargs')['time']

        if not date_to_set_unavailable or not time_to_set_unavailable:
            return Response({'Error': 'Date and time are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            date_to_cancel = datetime.strptime(date_to_set_unavailable, '%Y-%m-%d').date()

        except ValueError:
            return Response({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

        doctor = Doctor.objects.get(user=self.request.user)
        doctor.set_unavailable_time(date_to_set_unavailable, time_to_set_unavailable)

        return Response(f'Time {date_to_cancel} {time_to_set_unavailable} has been set unavailable', status=status.HTTP_200_OK)


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



