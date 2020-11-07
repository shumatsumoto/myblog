from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog


class BlogList(ListView):
	template_name = 'myapp/templates/blog_list.html'
	model = Blog
