from django.contrib import admin

from blog_app.models import Like, comment, post

# Register your models here.
admin.site.register(post)
admin.site.register(comment)
admin.site.register(Like)