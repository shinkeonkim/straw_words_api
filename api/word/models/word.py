from django.db import models
from config.models import BaseModel
from inflection import underscore

class WordManager(models.Manager):
  use_for_related_fields = True

  def get_queryset(self):
    return super().get_queryset().filter(lanh=underscore(self.model.__name__))


class Word(BaseModel):
  class Meta:
    managed = True
    db_table = 'words'
    verbose_name = 'Word'
    verbose_name_plural = 'Words'

  content = models.TextField(
    verbose_name="단어 내용"
  )
  type = models.CharField(
    verbose_name='언어',
    max_length=10,
    blank=True,
    null=True,
    default='korean_word',
  )
