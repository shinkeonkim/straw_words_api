from django.db import models
from config.models import BaseModel
from inflection import underscore

class WordManager(models.Manager):
  use_for_related_fields = True

  def get_queryset(self):
    return super().get_queryset().filter(lanh=underscore(self.model.__name__))


class Word(BaseModel):
  class Meta:
    verbose_name = 'word'
    verbose_name_plural = 'words'

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


class KoreanWord(Word):
  class Meta:
    proxy = True
    verbose_name = 'korean_word'
    verbose_name_plural = 'korean_words'
  
  def __init__(self, *args, **kwargs):
    self._meta.get_field('type').default = 'korean_word'
    super(KoreanWord, self).__init__(*args, **kwargs)


class EnglishWord(Word):
  class Meta:
    proxy = True
    verbose_name = 'english_word'
    verbose_name_plural = 'english_words'
  
  def __init__(self, *args, **kwargs):
    self._meta.get_field('type').default = 'english_word'
    super(EnglishWord, self).__init__(*args, **kwargs)
