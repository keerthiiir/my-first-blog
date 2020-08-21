from django import forms
from .models import Post
from .models import CVPost

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CVPostForm(forms.ModelForm):

    class Meta:
        model = CVPost
        fields = ('job_title', 'job_duration', 'job_description')