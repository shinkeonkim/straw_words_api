from django.contrib.auth.models import (AbstractBaseUser, AbstractUser,
                                        BaseUserManager, PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.models import BaseModel


class UserManager(BaseUserManager):
  def create_user(self, email, password, nickname):
    if not email:
      raise ValueError(_('Users must have an email address'))

    if not nickname:
      raise ValueError(_('Users must have an nickname'))

    user = self.model(
      email=self.normalize_email(email),
      nickname=nickname,
    )
    user.set_password(password)
    user.save()

    return user

  def create_superuser(self, email, nickname, password):
    user = self.create_user(
      email=email,
      nickname=nickname,
      password=password,
    )

    user.is_superuser = True
    user.save()

    return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'

  USERNAME_FIELD = 'nickname'

  nickname = models.CharField(
    null=False,
    max_length=20,
    unique=True,
  )
  email = models.EmailField()

  objects = UserManager()
  REQUIRED_FIELDS = ['email'] 

  @property
  def is_staff(self):
    return self.is_superuser
