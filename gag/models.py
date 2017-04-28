from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    


class Upload(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=250)
    user_pic=models.CharField(max_length=2050)
    description=models.CharField(max_length=250)
    file_format=models.CharField(max_length=10)
    media = models.FileField()
    upload_date=models.DateTimeField(default=datetime.now, blank=True)
    like=models.IntegerField(default=1)

    def __str__(self):
        return self.description+'-'+self.file_format


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_id = models.IntegerField()
    comment_time = models.DateTimeField(default=datetime.now, blank=True)
    comment = models.CharField(max_length=2000)

    def __str__(self):
        return self.comment


class Liked(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    like_id=models.IntegerField(default=0)
    description=models.CharField(max_length=250)


    def __str__(self):
        return self.description
