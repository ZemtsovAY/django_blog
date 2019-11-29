from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import *
from .forms import TagForm


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectListMixin:
    model = None
    template = None

    def get(self, request):
        obj = self.model.objects.all()
        return render(request, self.template, context={self.model.__name__.lower() + 's': obj})


class ObjectCreateMixin:
    form = None
    template = None

    def get(self, request):
        return render(request, self.template, context={'form': self.form})

    def post(self, request):
        bound_form = self.form(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, self.template, context={'form': bound_form})

class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        print(slug)
        return render(request, 'blog/tag_update.html', context={'form': bound_form, 'obj': obj})

    def post(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, 'blog/tag_update.html', context={'form': bound_form, 'obj': obj})

