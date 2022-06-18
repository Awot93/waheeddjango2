from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_date = models.DateField(default=timezone.now)
    published_date = models.DateField(default=timezone.now)

    def _str_(self):
        return self.title