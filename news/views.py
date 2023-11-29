from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .forms import NewsPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import NewsPost
from django.views.generic import DeleteView
from django.views.generic import DetailView


class IndexView(TemplateView):
    template_name = 'index.html'

@method_decorator(login_required, name='dispatch')
class CreateNewsView(CreateView):
    form_class = NewsPostForm
    template_name = "post_news.html"
    success_url = reverse_lazy('news:post_done')


    def form_valid(self,form):
        postdate = form.save(commit=False)
        postdate.user = self.request.user
        postdate.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

class IndexView(ListView):
    template_name = 'index.html'
    queryset = NewsPost.objects.order_by('-posted_at')
    paginate_by = 9


class CategoryView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = NewsPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name  ='index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = NewsPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name = 'detail.html'
    model = NewsPost

class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = NewsPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
    
class NewsDeleteView(DeleteView):
    model = NewsPost
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news:mypage')

    def delete(self,request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)