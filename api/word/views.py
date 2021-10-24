from django.shortcuts import render
from rest_framework.generics import ListAPIView

from config.views import BaseView

from .models.word import Word
from .serializers import WordSerializer
class WordListView(ListAPIView):
  serializer_class = WordSerializer
  queryset = Word.objects.all()
