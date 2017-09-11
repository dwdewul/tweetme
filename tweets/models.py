from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    text = models.CharField(max_length=256)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} -- {}".format(self.text, self.user.id)

    def get_absolute_url(self):
        return reverse('tweets:detail_view', args=[self.id])

    class Meta:
        ordering = ['-timestamp']
