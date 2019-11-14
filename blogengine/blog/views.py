from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View

from .models import Post
from .models import Tag

from .utils import ObjectDetailMixin
from .utils import ObjectListMixin

from .forms import TagForm


# Create your views here.
class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})




# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/index.html', context={'posts': posts})


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'blog/tags_list.html', context={'tags': tags})


# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'



class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'blog/tag_detail.html', context={'tag': tag})

