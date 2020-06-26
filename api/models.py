from django.db import models
from django.utils import timezone

class Post(models.Model):
    text = models.CharField(max_length=280)
    post_time = models.DateTimeField(default=timezone.now)
    is_boast = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.text
    

