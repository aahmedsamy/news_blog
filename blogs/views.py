import asyncio
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.
from .models import Category
from utilis.views import _header_context, merge_dicts


def index(request):
    return render(request, "home.html")


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = merge_dicts(context, _header_context())
        return context


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'blogs/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = merge_dicts(context, _header_context())
        return context
