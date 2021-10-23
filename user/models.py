from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, password, nickname=""):
        if not email:
            raise ValueError(_('Users must have an email address'))

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
        )

        user.is_superuser = True
        user.save()

        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
  USERNAME_FIELD = 'username'

  username = models.CharField(
    null=False,
    max_length=20,
  )
  email = models.EmailField()

  objects = UserManager()
