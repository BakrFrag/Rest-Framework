from rest_framework import generics;
from rest_framework import permissions;
from posts.serializers import PostSerializer,PostCreateSerializer;
from posts.models import Post;
from rest_framework import permissions;
class PostApiView(generics.ListAPIView):
    model=Post;
    queryset=Post.objects.all();
    serializer_class=PostSerializer;
class PostRetriveApiView(generics.RetrieveAPIView):
    # lookup_field='pk';
    queryset=Post.objects.all();
    model=Post;
    serializer_class=PostSerializer;
class PostCreateApiView(generics.CreateAPIView):
    model=Post;
    serializer_class=PostCreateSerializer;
    permission_classes=[permissions.AllowAny]
    def perform_create(self,serializer):
        if self.request.user.is_authenticated:
                 serializer.save(author=self.request.user)
class PostUpdateApiView(generics.RetrieveUpdateAPIView):
    model=Post;
    lookup_field="pk";
    serializer_class=PostCreateSerializer;
    queryset=Post.objects.all();
class PostDestoryApiView(generics.RetrieveDestroyAPIView):
    model=Post;
    lookup_field="pk";
    serializer_class=PostSerializer;
    queryset=Post.objects.all();