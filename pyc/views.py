# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class PycListView(ListView):
	model = Post
	template_name = 'home.html'

class PycDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'