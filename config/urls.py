"""Module for url settings of Project"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("user.urls", "user")),
    path("api/words/", include("api.word.urls", "word")),
]
