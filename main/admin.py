from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display=('rogophoto','id','jop','postname','author','write','created_date')




# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post, PostAdmin)
