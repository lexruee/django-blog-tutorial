from django.shortcuts import render, reverse
from django.views import generic, View
from django.utils import timezone
from django.http import Http404, HttpResponseRedirect

from .models import Post, Comment

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 5
    queryset = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        context['comments'] = Comment.objects.filter(post_id=post.id).order_by('-pub_date')
        return context

