from django.db import models

class Command(models.Model):
    DIFFICULTY_CHOICES = [
    ('Easy', 'Easy'),
    ('Intermediate', 'Intermediate'),
    ('Difficult', 'Difficult'),
    ('Not Rated', 'Not Rated'),
]
    title = models.CharField(max_length=300, blank=True, null=True)
    keyword = models.CharField(max_length=100, blank=True, null=True)
    command = models.TextField(max_length=300, blank=True, null=True)
    title_en = models.CharField(max_length=300, blank=True, null=True)
    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default="Not Rated",
    )
    date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural='Commands'

    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=300, blank=True, null=True)
    url=models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural='Articles'

    def __str__(self):
        return self.title
