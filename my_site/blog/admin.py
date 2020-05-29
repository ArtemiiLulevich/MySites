from django.contrib import admin

from .models import Post


# Simple admin page without customization.
admin.site.register(Post)

