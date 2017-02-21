
import datetime
from django.utils import timezone
from django.db import models


class Post(models.Model):

    # CHECK LATER THE UNIQUE = TRUE ?
    name = models.CharField(max_length=80, unique=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100, default="empty title", null=True)
    content= models.TextField(null=True)

    def __str__(self):
        return self.title + "by" + self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

