from django.db import models


class Federation(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    region = models.CharField(max_length=100, blank=False)
    emblem = models.ImageField()
    management = models.TextField(blank=False)


class TypeEvent(models.Model):
    title = models.CharField(max_length=100, blank=False)


class ClassEvent(models.Model):
    title = models.CharField(max_length=100, blank=False)


class Event(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    time_start = models.DateTimeField(blank=False)
    time_end = models.DateTimeField(blank=False)
    federation = models.ForeignKey(to='Federation', on_delete=models.CASCADE)
    region = models.CharField(max_length=100, blank=False)
    management = models.TextField(blank=False)
    type_event = models.ForeignKey(to='TypeEvent', on_delete=models.CASCADE)
    class_event = models.ForeignKey(to='ClassEvent', on_delete=models.CASCADE)


class Club(models.Model):
    title = models.CharField(max_length=100, blank=False)
    body = models.TextField(blank=False)
    emblem = models.ImageField()
    management = models.TextField(blank=False)
    federation = models.ForeignKey(to='Federation', on_delete=models.CASCADE)
    region = models.CharField(max_length=100, blank=False)


class Document(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    file = models.FileField()


class Team(models.Model):
    athletes = models.TextField(blank=False)
    trainer = models.TextField(blank=False)
    doctors = models.TextField(blank=False)