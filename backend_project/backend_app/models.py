from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=256, blank=True)
    password = models.CharField(max_length=250, blank=True)
    # token = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.username


class Url(models.Model):
    title = models.TextField(null=True)
    longUrl = models.TextField(null=True)
    shortUrl = models.TextField(null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
