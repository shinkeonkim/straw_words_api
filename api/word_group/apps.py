"""Module for app configs of word_group app"""

from django.apps import AppConfig


class WordGroupConfig(AppConfig):
    """AppConfig definition for WordGroupConfig."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api.word_group"
