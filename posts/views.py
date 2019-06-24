from rest_framework import generics,permissions,mixins;
from posts.serializers import PostSerializer,PostCreateSerializer;
from posts.models import Post;
from django.shortcuts import get_object_or_404;
class PostApiView(generics.ListCreateAPIView):
         model=Post;
         queryset=Post.objects.all();
    
    # def post(self,request,*args,**kwargs):
    #     serializer_class=PostCreateSerializer
    #     return self.create(request,*args,**kwargs);
    # def perform_create(self,serializer):
    #     return serializer.save(author=self.request.user);
         def get_serializer_class(self):
              if self.request.method=="GET" or self.request.method=="OPTIONS":
                return PostSerializer;
              else:
                    return PostCreateSerializer; 
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
class ApiWithMixins(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin,generics.ListAPIView):
            model=Post;
            
            def get_queryset(self):
                qs=Post.objects.all();
                q=self.request.GET.get('q',None);
                if q is not None:
                    return q.filter(content__icontains=q);
                return qs;
            def get_object(self):
               request=self.request;
               queryset=self.get_queryset();
               id=request.GET.get('id',None);
               if id is not None:
                   obj=get_object_or_404(Post,id=id);
                   self.check_object_permissions(request,obj);
               return obj;
            def get(self,request,*args,**kwargs):
                id=self.request.GET.get('id',None);
                if id is not None:
                    return self.retrieve(request,*args,**kwargs);
                return super().get(request,*args,**kwargs);
            def get_serializer_class(self):
                request=self.request;
                if request.method=="GET" or request.method=="OPTIONS" or request.method=="DELETE":
                    return PostSerializer
                else:
                    return PostCreateSerializer;
            def post(self,request,*args,**kwargs):
                return self.create(request,*args,**kwargs);
            def put(self,request,*args,**kwargs):
                return self.update(request,*args,**kwargs);
            def patch(self,request,*args,**kwargs):
                return self.update(request,*args,**kwargs);
            def delete(self,request,*args,**kwargs):
                return self.destroy(request,*args,**kwargs);



            


