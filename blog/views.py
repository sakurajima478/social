from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import PostModel
from .forms import PostFrom

# Create your views here.


@login_required
def posts_view(request):
    posts = PostModel.objects.all()
    form = PostFrom(request.POST or None, request.FILES)
    
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
            