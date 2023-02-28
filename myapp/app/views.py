from django.shortcuts import render
#from django.views import View
from .models import Post
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer
from rest_framework import generics
# Create your views here.
#class Get_all(View):
#    def get(self,request):
#        posts=Post.objects.all()
#        return render(request,'app/index.html', context={"posts":posts})
class PostsList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()