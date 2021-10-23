from rest_framework.serializers import ModelSerializer

class WordSerializer(ModelSerializer):
  class Meta:
    fields = [
      'content',
      'type',
    ]
