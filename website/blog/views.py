from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.utils import timezone
from django.http import Http404, HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentForm

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
        context['form'] = CommentForm
        context['comments'] = Comment.objects.filter(post_id=post.id).order_by('-pub_date')
        return context
    
def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        print("hello")
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        content = form.cleaned_data['content']
        comment = Comment(username=username, email=email, title=title, 
                content=content, pub_date=timezone.now(), post_id=post.id)
        comment.save()
        return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)))

    return HttpResponseRedirect(reverse('blog:detail', args=(post.id,)),
            {'form': form})

