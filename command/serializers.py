from rest_framework import serializers
from .models import Command, Article

class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = "__all__"

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"