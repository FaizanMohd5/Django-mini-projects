from django.db import models

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    post_description = models.CharField(max_length=200)
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.CharField(max_length=200)
    post_body = models.TextField()

