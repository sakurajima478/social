from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PostModel, Like
from .forms import PostFrom

# Create your views here.


@login_required
def posts_view(request):
    posts = PostModel.objects.all()
    form = PostFrom(request.POST or None, request.FILES)
        
    likes = Like.objects.filter(author=request.user)
    
     # Agregar información de likes a cada post
    for post in posts:
        post.user_like = likes.filter(post=post).first()
    
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.author = request.user
            new_user.save()
            messages.success(request, 'Post published successfully!')
            return redirect('blog:posts')
        
        else:
            messages.warning(request, 'data not valid!')

    return render(request, 'pages/blog/posts.html', context={
        'posts' : posts,
        'form' : form,
    })

@login_required
def like(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    like_qs = Like.objects.filter(author=request.user, post=post)

    if like_qs.exists():
        like_qs[0].delete()
    else:
        Like.objects.create(author=request.user, post=post)

    return redirect('blog:posts')
