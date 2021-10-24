"""Module for model of word_group app"""

from django.db import models

from api.word.models.word import Word
from config.models import BaseModel


class WordGroup(BaseModel):
    """Model definition for WordGroup."""

    class Meta:
        """Meta definition for WordGroup."""

        db_table = "word_groups"
        managed = True
        verbose_name = "WordGroup"
        verbose_name_plural = "WordGroups"

    words = models.ManyToManyField(
        Word,
        related_name="words",
    )

    def __str__(self):
        pass
