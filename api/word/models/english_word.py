"""English Word Model File"""
from .word import Word


class EnglishWord(Word):
    """Model definition for EnglishWord."""

    class Meta:
        """Meta definition for EnglishWord."""

        proxy = True
        managed = True
        db_table = "english_words"
        verbose_name = "EnglishWord"
        verbose_name_plural = "EnglishWords"

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "english_word"
        super().__init__(*args, **kwargs)
