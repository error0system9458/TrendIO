from rest_framework import generics
from home.models import Post
from .serializers import PostSerializer


class PostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer


    def get_queryset(self):
        return Post.objects.all()
