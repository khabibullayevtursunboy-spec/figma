from django.db import models
from django.contrib.auth.models import User


class Massage(models.Model):
    user = models.ForeignKey(User)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Birinchisahifa(models.Model):
    kattamatn=models.CharField(max_length=800)
    kichikmatn=models.TextField()
    yuklashmatni = models.CharField(max_length=200)

    def __str__(self):
        return self.kattamatn

class Appdownload(models.Model):