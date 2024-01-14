from django.shortcuts import render
from django.views.generic import ListView, DetailView

from postings.models import Posting


class IndexView(ListView):
    template_name = "postings/index.html"
    model = Posting
    paginate_by = 30


class PostingDetailView(DetailView):
    model = Posting
    template_name = "postings/detail.html"
