from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    return render(request, "blog/home.html")  # New home template


# List all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create post
def post_create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        return redirect('post_list')
    return render(request, 'blog/post_form.html')

# Update post
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_list')
    return render(request, 'blog/post_form.html', {'post': post})

# Delete post
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})


