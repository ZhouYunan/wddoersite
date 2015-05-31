# coding:utf-8
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    email = models.EmailField('email address', unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
