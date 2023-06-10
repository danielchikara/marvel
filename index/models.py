from django.db import models

# Create your models here.


class Comic(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=160)
    thumbnail = models.CharField(max_length=1000)
    series = models.CharField(max_length=160)
    date = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return self.title


class Creators(models.Model):
    comic = models.ForeignKey(
        Comic, related_name="comic_creators", on_delete=models.CASCADE,  null=True)
    name = models.CharField(max_length=160)
    role = models.CharField(max_length=160)

    def __str__(self) -> str:
        return self.role
