from django.db import models
from django.utils.timezone import now

# Create your models here.

class Todo(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(default=now) 