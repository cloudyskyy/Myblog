# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
# Create your models here.
class Comment(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=225)
    url=models.URLField(blank=True)
    text=models.TextField()
    createdTime=models.DateTimeField(auto_now_add=True)

    post=models.ForeignKey('blog.Post')

    def __unicode__(self):return self.text[:20]