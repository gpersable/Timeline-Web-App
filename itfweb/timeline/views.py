from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, PostComment

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'timeline/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comment = PostComment(request.POST or None)
    if request.user.is_authenticated:
        if comment.is_valid():
            post_comment = comment.save(commit=False)
            post_comment.commented_post = post
            post_comment.commenter = request.user
            post_comment.save()
            return redirect('timeline:detail', post_id)

        comments = Comment.objects.filter(commented_post = post)
        return render(request, 'timeline/detail.html', {'post': post,'comment': comment,'comments': comments})
    else:
        return redirect('login')

def create_post(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST or None)
        if form.is_valid():
            post_create = form.save(commit=False)
            post_create.user = request.user
            post_create.save()
            return redirect('timeline:index')

        return render(request, 'timeline/new-post.html', {'form':form})
    else:
        return redirect('login')
