from django.forms import ModelForm
from .models import NewsPost
from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList


class NewsPostForm(ModelForm):

    class Meta:
        model = NewsPost
        fields = ['category','title','comment','image1','image2']

class ContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
        'お名前を入力して下さい'
        self.fields['name'].widget.attrs['class'] = 'form-control'


        self.fields['email'].widget.attrs['placeholder'] = \
        'メールを入力してください'
        self.fields['email'].widget.attrs['class'] = 'form-control'


        self.fields['title'].widget.attrs['placeholder'] = \
        'タイトルを入力してください'
        self.fields['title'].widget.attrs['class'] = 'form-control'



        self.fields['message'].widget.attrs['placeholder'] = \
        'メッセージを入力してください'
        self.fields['message'].widget.attrs['class'] = 'form-control'
