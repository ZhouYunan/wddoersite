# coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """
    Custom my user class for wddoer.com site
    http://blackglasses.me/2013/09/17/custom-django-user-model/
    """
    email = models.EmailField(unique=True, db_index=True, verbose_name="email address")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    def __unicode__(self):
        return self.email
