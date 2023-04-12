from django.urls import path

from .views.password_reset import PasswordResetRequestView
from .views.password_reset import PasswordResetConfirmView
from .views.registration import RegistrationView
from .views.registration import ConfirmRegistrationView
from .views.login import LoginView
from .views.logout import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('register-user/', RegistrationView.as_view(), name='register-user'),
    path('register-user-confirm/', ConfirmRegistrationView.as_view(), name='register-user-confirm'),
    path('login-user/', LoginView.as_view(), name='login-user'),
    path('logout-user/', LogoutView.as_view(), name='logout-user'),

]
