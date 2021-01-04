from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Create your views here.
from .models import Category
from utilis.views import HomeContext, HeaderContext


def index(request):
    return render(request, "home.html")


class TestPageView(TemplateView):
    template_name = "test.html"


class HomePageView(TemplateView):
    template_name = "home.html"
    extra_context = {**HomeContext(), **HeaderContext()}


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'blogs/category_detail.html'
    extra_context = HeaderContext()
