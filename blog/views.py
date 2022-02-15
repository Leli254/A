from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView,CreateView

from .models import Post, PostCategory,PostTag

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    
    
    
class PostCategoryList(ListView):
    model = PostCategory
    template_name = 'blog/post_category_list.html'
    
class PostCategoryDetail(DetailView):
    model = PostCategory
    template_name = 'blog/post_category_detail.html'
    
    
class PostTagList(ListView):
    model = PostTag
    template_name = 'blog/post_tag_list.html'
    
    
class PostTagDetail(DetailView):
    model = PostTag
    template_name = 'blog/post_tag_detail.html'



class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content', 'category', 'tag']
    template_name = 'blog/post_create.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)