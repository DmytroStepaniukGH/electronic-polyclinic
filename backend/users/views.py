from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from .serializers import DoctorListSerializer
from .models import Doctor


@extend_schema(
    tags=['Doctors'],
)
class DoctorsListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DoctorListSerializer

    def get_queryset(self):
        queryset = Doctor.objects.all()

        return queryset
