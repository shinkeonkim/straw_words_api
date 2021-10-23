from django.db import models

class BaseModel(models.Model):
  created_at = models.DateTimeField(
    auto_now_add=True
  )
  updated_at = models.DateTimeField(
    auto_now=True
  )

  def __str__(self):
    pass

  class Meta:
    abstract = True
    verbose_name = 'BaseModel'
    verbose_name_plural = 'BaseModels'
