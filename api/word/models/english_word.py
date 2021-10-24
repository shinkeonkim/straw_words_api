from .word import Word

class EnglishWord(Word):
  class Meta:
    proxy = True
    managed = True
    db_table = 'english_words'
    verbose_name = 'EnglishWord'
    verbose_name_plural = 'EnglishWords'
  
  def __init__(self, *args, **kwargs):
    self._meta.get_field('type').default = 'english_word'
    super(EnglishWord, self).__init__(*args, **kwargs)
