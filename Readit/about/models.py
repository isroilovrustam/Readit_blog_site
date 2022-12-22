from django.db import models


# Create your models here.


class About(models.Model):
    image = models.ImageField()
    video = models.FileField(null=True, blank=True)
    title = models.CharField(max_length=202)
    content = models.TextField()
    mission = models.CharField(max_length=303)
    vision = models.CharField(max_length=303)
    value = models.CharField(max_length=303)

    def __str__(self):
        return self.title
