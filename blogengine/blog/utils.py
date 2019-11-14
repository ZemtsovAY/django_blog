from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *


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
        print(obj)
        return render(request, self.template, context={self.model.__name__.lower() + 's': obj})


