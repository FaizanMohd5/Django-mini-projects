from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id','post_title','post_description','post_date','post_author','post_body']
