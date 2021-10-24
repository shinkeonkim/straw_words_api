"""Module for word model"""

from django.db import models
from django.db.models.query import QuerySet
from inflection import underscore

from config.models import BaseModel


class WordManager(models.Manager):
    """ModelManger definition for Word."""

    use_for_related_fields = True

    def get_queryset(self) -> QuerySet:
        """Return Default Word Model QuerySet"""
        return super().get_queryset().filter(lanh=underscore(self.model.__name__))


class Word(BaseModel):
    """Model definition for Word."""

    class Meta:
        """Meta definition for Word."""

        managed = True
        db_table = "words"
        verbose_name = "Word"
        verbose_name_plural = "Words"

    content = models.TextField(verbose_name="단어 내용")
    type = models.CharField(
        verbose_name="언어",
        max_length=10,
        blank=True,
        null=True,
        default="korean_word",
    )
