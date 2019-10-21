from django.contrib import admin
from blog.models import Post

# Register your models here.
admin.site.site_header = 'Blog Admin'

admin.site.register(Post)


