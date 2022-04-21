from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db import models

from account.managers import CustomUserManager

JOB_TYPE = (
    ('M', "Male"),
    ('F', "Female"),
)

ROLE = (
    ('employer', "Employer"),
    ('employee', "Employee"),
)

def validate_file_extension(value):
    if (value.file.content_type != 'application/pdf' or value.file.content_type != 'application/msword'):
        raise ValidationError(u'Incompatible file type')
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    role = models.CharField(choices=ROLE,  max_length=10)
    gender = models.CharField(choices=JOB_TYPE, max_length=1)

    resume = models.FileField(upload_to='media', null=True, blank=True, verbose_name='Resume', validators=[validate_file_extension])
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name+ ' ' + self.last_name
    objects = CustomUserManager()
