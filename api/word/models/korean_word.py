"""Module for korean word model"""

from .word import Word


class KoreanWord(Word):
    """Model definition for KoreanWord."""

    class Meta:
        """Meta definition for KoreanWord."""

        proxy = True
        managed = True
        db_table = "korean_words"
        verbose_name = "KoreanWord"
        verbose_name_plural = "KoreanWords"

    def __init__(self, *args, **kwargs):
        self._meta.get_field("type").default = "korean_word"
        super().__init__(*args, **kwargs)
