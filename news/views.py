from django.shortcuts import render
from datetime import datetime

from django.views.generic import ListView, DetailView

from .models import Article

class ArticleList(ListView):

    model = Article
    ordering = '-data'
    template_name = 'news.html'
    context_object_name = 'Articles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class ArticleDetail(DetailView):

    model = Article
    template_name = 'Article.html'
    context_object_name = 'Article'