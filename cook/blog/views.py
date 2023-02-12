from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


def home(request):
    return render(request, 'base.html')
