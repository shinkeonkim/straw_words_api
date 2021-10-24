from .word import Word

class KoreanWord(Word):
  class Meta:
    proxy = True
    managed = True
    db_table = 'korean_words'
    verbose_name = 'KoreanWord'
    verbose_name_plural = 'KoreanWords'
  
  def __init__(self, *args, **kwargs):
    self._meta.get_field('type').default = 'korean_word'
    super(KoreanWord, self).__init__(*args, **kwargs)
