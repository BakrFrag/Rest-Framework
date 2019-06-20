from django.contrib import admin
from posts.models import Post;
from posts.forms import PostForm
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    form=PostForm
    list_display=['author','title','content','image']
admin.site.register(Post,PostAdmin);