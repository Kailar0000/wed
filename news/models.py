from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100, blank=False)
    time = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)