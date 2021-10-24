"""Project Base Views"""
from typing import Union

from django.contrib.auth.models import AnonymousUser, User
from django.views import View


class BaseView(View):
    """View definition for BaseView."""

    def current_user(self) -> Union[User, AnonymousUser]:
        """Return request.user -> Union[User, AnonymousUser]"""

        return self.request.user

    def is_anonymous_user(self) -> bool:
        """Return whether the user is anonymous."""

        return self.request.user.is_anonymous

    def is_authenticated_user(self) -> bool:
        """Return wherther the user is authenticated"""
        return self.request.user.is_authenticated
