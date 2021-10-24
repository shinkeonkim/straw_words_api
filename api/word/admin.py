"Module for Admin View of word app"

from django.contrib import admin

from .models.english_word import EnglishWord
from .models.korean_word import KoreanWord
from .models.word import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """Admin View for Word"""

    # list_display = ('',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(KoreanWord)
class KoreanWordAdmin(admin.ModelAdmin):
    """Admin View for KoreanWord"""

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #   Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(EnglishWord)
class EnglishWordAdmin(admin.ModelAdmin):
    """Admin View for KoreanWord"""

    # list_display = ('',)
    # list_filter = ('',)
    # inlines = [
    #   Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
