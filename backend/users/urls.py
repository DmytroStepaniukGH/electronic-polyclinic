from django.urls import path
from .views import CreateAppointmentView, AppointmentListView, AvailableSlotsView, AllSpecializations, \
    DoctorsListViewSet, SearchAPIView, FilterDoctors, CancelAppointmentView, SetUnavailableTimeView, \
    CloseAppointmentView, DoctorView

urlpatterns = [
    path('new-appointment/<int:doctor_id>/<str:date>/<str:time>', CreateAppointmentView.as_view(), name='new-appointment'),
    path('close-appointment/', CloseAppointmentView.as_view(), name='close-appointment'),
    path('appointments/', AppointmentListView.as_view(), name='appointments'),
    path('cancel-appoitment/<str:date>/<str:time>', CancelAppointmentView.as_view(), name='cancel-appointment'),
    path('available-slots/<int:doctor_id>/<str:date>', AvailableSlotsView.as_view(), name='available-slots'),
    path('set-unavailable-time/<str:date>/<str:time>', SetUnavailableTimeView.as_view(), name='set-unavailable-time'),
    path('specializations/', AllSpecializations.as_view({'get': 'list'}), name='specializations'),
    path('doctors/', DoctorsListViewSet.as_view({'get': 'list'}), name='doctors'),
    path('doctors/doctor-<int:doctor_id>', DoctorView.as_view(), name='doctor'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('filter-doctors/<str:specialization>', FilterDoctors.as_view({'get': 'list'}), name='filter-doctors'),
]
