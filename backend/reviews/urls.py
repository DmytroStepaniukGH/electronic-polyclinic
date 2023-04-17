from django.urls import path

from reviews.views.finished_visites import FinishedAppointmentsListView # noqa
from reviews.views.finished_visites import FinishedAppointmentView # noqa
from reviews.views.create_review import CreateReviewView # noqa

urlpatterns = [
    path('finished/', FinishedAppointmentsListView.as_view(), name='finished-appointments'),
    path('finished/id-<int:appointment_id>', FinishedAppointmentView.as_view(), name='appointment'),
    path('finished/id-<int:appointment_id>/add-review', CreateReviewView.as_view(), name='add-review'),
]
