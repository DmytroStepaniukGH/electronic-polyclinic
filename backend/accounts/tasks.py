from urllib.parse import urljoin

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
<<<<<<< HEAD

from accounts.utils import encode_uid # noqa
from backend.celery import app # noqa
=======
from django.core.mail import send_mail, EmailMessage

from accounts.utils import encode_uid # noqa
from backend.celery import app # noqa
from backend.settings import EMAIL_HOST_USER # noqa
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6


@app.task()
def send_email_for_password_reset(user_id: int):
    user = get_user_model().objects.only('email').get(pk=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=('last_login',))

    uid = encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    link = urljoin(
        settings.FRONTEND_HOST,
        settings.FRONTEND_PASSWORD_RESET_PATH.format(uid=uid, token=token),
    )

    print(link, flush=True)


@app.task()
def send_email_for_registration_confirm(user_id: int):
    user = get_user_model().objects.only('email').get(pk=user_id)
<<<<<<< HEAD
    # user.last_login = timezone.now()
    # user.save(update_fields=('last_login',))

=======
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6
    uid = encode_uid(user.pk)
    token = default_token_generator.make_token(user)

    link = urljoin(
        settings.FRONTEND_HOST,
        settings.FRONTEND_REGISTRATION_CONFIRM_PATH.format(uid=uid, token=token),
    )

    print(link, flush=True)
<<<<<<< HEAD
=======

    message = f'Hello. To confirm your account click this link: {link}'
    send_mail(
        subject='Confirmation link',
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user]
    )
>>>>>>> 2a67131b69271284b976cb5304854fdb0c03f3d6
