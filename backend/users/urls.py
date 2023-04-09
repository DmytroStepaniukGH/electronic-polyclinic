from django.urls import path
from .views import CreateAppointmentView, AppointmentListView, AvailableSlotsView, AllSpecializations, \
    DoctorsListViewSet, SearchAPIView, FilterDoctors, CancelAppointmentView, SetUnavailableTimeView

urlpatterns = [
    path('new-appointment/<doctor_id>/<date>/<time>', CreateAppointmentView.as_view(), name='new-appointment'),
    path('appointments/', AppointmentListView.as_view(), name='appointments'),
    path('cancel-appoitment/<date>/<time>', CancelAppointmentView.as_view(), name='cancel-appointment'),
    path('available-slots/<doctor_id>/<date>', AvailableSlotsView.as_view(), name='available-slots'),
    path('set-unavailable-time/<date>/<time>', SetUnavailableTimeView.as_view(), name='set-unavailable-time'),
    path('specializations/', AllSpecializations.as_view(), name='specializations'),
    path('doctors/', DoctorsListViewSet.as_view({'get': 'list'}), name='doctors'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('filter-doctors/<specialization>', FilterDoctors.as_view({'get': 'list'}), name='filter-doctors'),
]
