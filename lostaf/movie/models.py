from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='movie/images', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    # 🔥 Nuevos campos:
    genre = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
