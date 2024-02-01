from typing import Any
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractBaseUser
from django.db import models


class U_Manager(UserManager):

    def create_user(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            email=email,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
        return self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='First name:', max_length=128)
    last_name = models.CharField(verbose_name='Last name:', max_length=128)
    email = models.EmailField(verbose_name='Email', unique=True)
    username = models.CharField(verbose_name='Username:', max_length=50, null=True, blank=True)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = U_Manager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    

