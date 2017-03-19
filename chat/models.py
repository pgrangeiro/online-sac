from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)


class Message(models.Model):
    room = models.ForeignKey(Room)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
