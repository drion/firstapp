from __future__ import unicode_literals

from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    minutes = models.IntegerField()
    seconds = models.IntegerField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

