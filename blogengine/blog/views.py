from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View

from .models import Post
from .models import Tag

from .utils import ObjectDetailMixin
from .utils import ObjectListMixin
from .utils import ObjectCreateMixin

from .forms import TagForm
from .forms import PostForm


# Create your views here.
class PostList(ObjectListMixin, View):
    model = Post
    template = 'blog/index.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    form = PostForm
    template = 'blog/post_create.html'


class TagList(ObjectListMixin, View):
    model = Tag
    template = 'blog/tags_list.html'


class TagCreate(ObjectCreateMixin, View):
    form = TagForm
    template = 'blog/tag_create.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagUpdate(View):
    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        tag = get_object_or_404(Tag, slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        print(slug)
        return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})

    def post(self, request, slug):
        tag = get_object_or_404(Tag, slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_update.html', context={'form': bound_form, 'tag': tag})




