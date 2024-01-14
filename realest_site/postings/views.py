from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from requests import post

from postings.models import Posting


class IndexView(ListView):
    template_name = "postings/index.html"
    model = Posting
    paginate_by = 30


def request_crawl(request):
    scrapy_settings = settings.SCRAPY
    scrapy_request = f"http://{scrapy_settings['host']:s}:{scrapy_settings['port']:s}/schedule.json"
    response = post(scrapy_request, data={'project': 'realest_scrap', 'spider': 'sreality', 'scrap_limit': 30})
    r_json = response.json()
    if r_json['status'] == 'error':
        return render(
            request,
            "postings/index.html",
            {
                "error_message": r_json['message']
            }
        )
    return HttpResponseRedirect(reverse('index'))


class PostingDetailView(DetailView):
    model = Posting
    template_name = "postings/detail.html"
