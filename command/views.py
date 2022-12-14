from .models import Command, Article
from .serializers import CommandSerializer, ArticleSerializer
from rest_framework import viewsets

class CommandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer