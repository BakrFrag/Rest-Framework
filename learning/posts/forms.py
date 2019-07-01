from django import forms;
from posts.models import Post;
class PostForm(forms.ModelForm):
    class Meta:
        model=Post;
        fields=['author','title','content','image'];
    def clean(self,*args,**kwargs):
        data=self.cleaned_data;
        title=data.get('title',None);
        content=data.get('content',None);
        image=data.get('image',None);
        author=data.get('author',None);
        if author is None or title is None or image is None or content is None:
           raise forms.ValidationError("This Field Can't Be Empty");
        return super().clean(*args,**kwargs);
        