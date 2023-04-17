from django.urls import path

from patientcard.views.patientcard_info import PatientCardInfoView # noqa

urlpatterns = [
    path('patient-card-<card_id>/', PatientCardInfoView.as_view(), name='patient-card'),
]
