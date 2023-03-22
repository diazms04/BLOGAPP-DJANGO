from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['subtitle'].widget.attrs.update({'class': 'form-control'})
        self.fields['cover_image'].widget.attrs.update({'class': 'form-control'})