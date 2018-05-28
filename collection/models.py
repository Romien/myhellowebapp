from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return u"%s %s" % (self.name, self.description)
