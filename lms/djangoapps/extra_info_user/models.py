from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator

USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True)
    educational_centre_code = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{0,8}$')])
