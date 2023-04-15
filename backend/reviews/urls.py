from django.urls import path

from .views.finished_visites import FinishedAppointmentsListView
from .views.finished_visites import FinishedAppointmentView
from .views.create_review import CreateReviewView

urlpatterns = [
    path('finished/', FinishedAppointmentsListView.as_view(), name='finished-appointments'),
    path('finished/id-<appointment_id>', FinishedAppointmentView.as_view(), name='appointment'),
    path('finished/id-<appointment_id>/add-review', CreateReviewView.as_view(), name='add-review'),
]
