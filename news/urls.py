from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('post/',views.CreateNewsView.as_view(),name='post'),

    path('post_done/',
         views.PostSuccessView.as_view(),
         name  = 'post_done'),

    path('news/<int:category>',
         views.CategoryView.as_view(),
         name = 'news_cat'),

     path('user-list/<int:user>',
          views.UserView.as_view(),
          name = 'user_list'),

     path('news-detail/<int:pk>',
          views.DetailView.as_view(),
          name = 'news_detail'),

     path('mypage/', views.MypageView.as_view(), name = 'mypage'),

     path('news/<int:pk>/delete/',
          views.NewsDeleteView.as_view(),
          name = 'news_delete'
          ),

     path(
         'contact/',
         views.ContactView.as_view(),
         name='contact'
     ),
]