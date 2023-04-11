from django.urls import path
from .views import AppointmentCreateView, AppointmentListView, AvailableSlotsView, AllSpecializations, \
    DoctorsListViewSet, SearchAPIView, FilterDoctors, DoctorView

urlpatterns = [
    path('new-appointment/', AppointmentCreateView.as_view(), name='new-appointment'),
    path('appointments/', AppointmentListView.as_view(), name='appointments'),
    path('available-slots/<doctor_id>/<date>', AvailableSlotsView.as_view(), name='available-slots'),
    path('specializations/', AllSpecializations.as_view(), name='specializations'),
    path('doctors/', DoctorsListViewSet.as_view({'get': 'list'}), name='doctors'),
    path('doctors/doctor-<doctor_id>', DoctorView.as_view(), name='doctor'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('filter-doctors/<specialization>', FilterDoctors.as_view({'get': 'list'}), name='filter-doctors'),
]
