from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Tag
import markdown
from comments.forms import CommentForm
# Create your views here.

def index(request):
    post_list=Post.objects.all().order_by('-create_time')
    context={
        'title':'my blog site',
        'post_list': post_list
    }
    obj=render(request,'diao/index.html',context)
    return obj

def detial(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.body=markdown.markdown(post.body,
                                extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc'
                                ])
    form=CommentForm()
    comment_list=post.comment_set.all()
    context={
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    obj=render(request,'diao/detial.html',context=context)
    return obj

def archives(request,year,month):
    post_list=Post.objects.fliter(create_time__year=year,
                                  create_time__month=month
                                  ).order_by('-create_time')
    obj=render(request,'diao/index.html',context={'post_list':post_list})
    return obj

def category(request,pk):
    cate=get_object_or_404(Category,pk=pk)
    post_list=Post.objects.fliter(category=cate).order_by('-create_time')
    obj=render(request,'blog/index.html',context={'post_list':post_list})
    return obj


