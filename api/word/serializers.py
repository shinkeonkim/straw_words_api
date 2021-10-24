"""Word App Serializers"""
from rest_framework.serializers import ModelSerializer


class WordSerializer(ModelSerializer):
    """Serializer definition for Word Model"""

    class Meta:
        """Meta definition for WordSerializer."""

        fields = [
            "content",
            "type",
        ]
