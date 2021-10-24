"""Module for url settings of word app"""
from django.urls import path

from .views import WordListView

app_name = "api.word"

urlpatterns = [
    path("", WordListView.as_view()),
]
