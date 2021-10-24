"""Module for Views of word app"""
from rest_framework.generics import ListAPIView

from config.views import BaseView

from .models.word import Word
from .serializers import WordSerializer


class WordListView(BaseView, ListAPIView):
    """View definition for WordListView."""

    serializer_class = WordSerializer
    queryset = Word.objects.all()
