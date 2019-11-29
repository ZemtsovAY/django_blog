from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View

from .models import Post
from .models import Tag

from .utils import ObjectDetailMixin
from .utils import ObjectListMixin
from .utils import ObjectCreateMixin
from .utils import ObjectUpdateMixin

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


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'






