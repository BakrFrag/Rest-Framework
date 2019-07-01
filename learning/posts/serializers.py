from posts.models import Post;
from rest_framework import serializers;
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post;
        fields=['pk','author','title','content','image'];
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post;
        fields=['title','content','image'];
    
