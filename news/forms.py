from django.forms import ModelForm
from .models import NewsPost

class NewsPostForm(ModelForm):

    class Meta:
        model = NewsPost
        fields = ['category','title','comment','image1','image2']