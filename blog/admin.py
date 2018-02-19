# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Post,Category,Tag

from django.contrib import admin

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_display=['title','createdTime','modifiedTime','category','author']

admin.site.register(Post,postAdmin)
admin.site.register(Category)
admin.site.register(Tag)