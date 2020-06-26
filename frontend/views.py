from django.shortcuts import render
from api.views import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'frontend/index.html', {'posts': posts})