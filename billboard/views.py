from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
import datetime
from models import Post

@login_required

def index(request):

    latest_post_list = Post.objects.order_by('-pub_date')[:5]

    return render(request, 'billboard/index.html',  {"posts": latest_post_list})


def newpost(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    content = request.POST.get('content')
    new_post = Post(title=title, name=author, content=content)
    new_post.save()
    context = {'new_post': new_post}
    return redirect('index')




