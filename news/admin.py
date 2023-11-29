from django.contrib import admin

from .models import Category, NewsPost

class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('id','title')
    list_display_links = ('id','title')

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(Category,CategoryAdmin)
admin.site.register(NewsPost,NewsPostAdmin)
