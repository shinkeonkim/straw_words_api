"""Module for models of user app"""

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.models import BaseModel


class UserManager(BaseUserManager):
    """ModelManger definition for User."""

    def create_user(self, email, nickname, password):
        """Create new user"""
        if not email:
            raise ValueError(_("Users must have an email address"))

        if not nickname:
            raise ValueError(_("Users must have an nickname"))

        user = self.model(
            email=self.normalize_email(email),
            nickname=nickname,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, nickname, password):
        """Create new admin user"""
        user = self.create_user(
            email=email,
            nickname=nickname,
            password=password,
        )

        user.is_superuser = True
        user.save()

        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    class Meta:
        """Meta definition for User."""

        managed = True
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD = "nickname"

    nickname = models.CharField(
        null=False,
        max_length=20,
        unique=True,
    )
    email = models.EmailField()

    objects = UserManager()
    REQUIRED_FIELDS = ["email"]

    @property
    def is_staff(self):
        """Return whether the user is staff
        - used to admin site
        """
        return self.is_superuser
