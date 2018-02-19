# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

# Create your views here.
def postComment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)

    if request.method=='POST':
        form=CommentForm(request.POST)

        if form.is_valid():
            comment=form.save(commit=False)

            comment.post=post

            comment.save()

            return redirect(post)

        else:
            commentList=post.comment_set.all()
            return render(request,'blog/detail.html',context={
                'post':post,
                'form':form,
                'commentList':commentList
            })
