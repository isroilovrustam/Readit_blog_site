from django.db import models


# Create your models here.


class Home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=202)
    text = models.TextField()

    def __str__(self):
        return self.title


class Article_home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class About_home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Contact_home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title


class Single_home(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=202)

    def __str__(self):
        return self.title