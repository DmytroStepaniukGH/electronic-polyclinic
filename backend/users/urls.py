from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import DoctorsListViewSet


app_name = 'products'

router = DefaultRouter()
router.register('doctors', DoctorsListViewSet, basename='doctors')

urlpatterns = [
    path('', include(router.urls)),
]