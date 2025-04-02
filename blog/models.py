from django.db import models
from django.utils.timezone import now
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    desc = models.TextField()
    img = models.ImageField(upload_to='blogs')
    comment = models.TextField()
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now())
    updated_at = models.DateTimeField(default=now())