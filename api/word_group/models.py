from django.db import models

from config.models import BaseModel

class WordGroup(BaseModel):
  def __str__(self):
    pass

  class Meta:
    db_table = 'word_groups'
    managed = True
    verbose_name = 'WordGroup'
    verbose_name_plural = 'WordGroups'
