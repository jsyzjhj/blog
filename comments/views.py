from django.shortcuts import render,get_object_or_404,redirect
from diao.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    post=get_object_or_404(Post,pk=post_pk)
    if request.method=='Post':
        form=CommentForm(request.Post)
        if form.is_valid():
            comment=form.save(comment=False)
            comment.post=post
            comment.save()
            return redirect(post)
        else:
            comment_list=post.comment_set.all()
            context={
                'post':post,
                'form':form,
                'comment_list':comment_list
            }
            obj=render(request,'diao/detial.html',context=context)
            return obj
    return redirect(post)
