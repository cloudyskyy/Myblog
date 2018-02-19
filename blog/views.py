# -*- coding: utf-8 -*-
from django.shortcuts import render


from django.http import HttpResponse
import markdown
from django.shortcuts import render,get_object_or_404
from comments.forms import CommentForm
from .models import Post,Category

# Create your views here.

def index(request):
    postList=Post.objects.all().order_by('-createdTime')
    return render(request, 'blog/index.html', context={
        'postList':postList
    })

def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body=markdown.markdown(post.body,['extra','codehilite','toc',])
    form=CommentForm()
    commentList=post.comment_set.all()
    return render(request,'blog/detail.html',context={'post':post,
                                                      'form':form,
                                                      'commentList':commentList})

def archives(request,year,month):
    postList=Post.objects.filter(createdTime__year=year,createdTime__month=month).order_by('-createdTime')
    return render(request,'blog/index.html',context=
    {'postList':postList})

def category(request, pk):
    cat=get_object_or_404(Category,pk=pk)
    postList=Post.objects.filter(category=cat).order_by('-createdTime')
    return render(request,'blog/index.html',context={
        'postList':postList
    })