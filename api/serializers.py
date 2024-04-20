from rest_framework import serializers
from .models import Story


class StorySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Story
        fields = ['id', 'headline', 'category', 'region', 'author', 'date', 'details']
