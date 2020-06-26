from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, PostSerializer
from .models import Post
from rest_framework.decorators import action
from django.http import HttpResponseRedirect

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def create(self, request):
        if request.method == 'POST':
            serializer = PostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            
    @action(detail=True, methods=['post'])
    def upvote(request, post_id):
        if request.method == 'POST':
            post = Post.objects.get(pk=post_id)
            post.votes += 1
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    @action(detail=True, methods=['post'])
    def downvote(request, post_id):
        if request.method == 'POST':
            post = Post.objects.get(pk=post_id)
            post.votes -= 1
            post.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
