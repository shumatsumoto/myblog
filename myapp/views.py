from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse, reverse_lazy


class BlogList(ListView):
	template_name = 'myapp/templates/blog_list.html'
	model = Blog


class BlogDetail(DetailView):
	template_name = 'myapp/templates/blog_detail.html'
	model = Blog


class BlogCreate(CreateView):
	template_name = 'myapp/templates/blog_form.html'
	model = Blog
	fields = ['title', 'content']

	def get_success_url(self):
		return reverse('blog_list')


class BlogUpdate(UpdateView):
	template_name = 'myapp/templates/blog_form.html'
	model = Blog
	fields = ['title', 'content']

	def get_success_url(self):
		return reverse('blog_detail', kwargs={'pk': self.object.pk})


class BlogDelete(DeleteView):
	template_name = 'myapp/templates/blog_confirm_delete.html'
	model = Blog

	success_url = reverse_lazy('blog_list')
