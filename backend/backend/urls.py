from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

api = [
<<<<<<< HEAD
    path('', include('users.urls')),
    path('accounts/', include('accounts.urls')),

=======
    path('', include('doctors.urls')),
    path('', include('accounts.urls')),
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
