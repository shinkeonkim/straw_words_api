"""Project Base Model Classes"""

from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Unicode representation of BaseModel."""
        return ""

    class Meta:
        """Meta definition for BaseModel."""

        abstract = True
        verbose_name = "BaseModel"
        verbose_name_plural = "BaseModels"
