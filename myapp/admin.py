from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
	list_display = ('title', 'content',)

admin.site.register(models.Blog, BlogAdmin)
