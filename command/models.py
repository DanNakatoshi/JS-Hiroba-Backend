from django.db import models


class Command(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    command = models.TextField(max_length=300, blank=True, null=True)

    class Meta:
        verbose_name_plural='Commands'

    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=300, blank=True, null=True)
    url=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural='Articles'

    def __str__(self):
        return self.title
