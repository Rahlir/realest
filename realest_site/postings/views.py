from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from requests import post, get

from postings.models import Posting
from postings.requests import input_to_category


class IndexView(ListView):
    template_name = "postings/index.html"
    model = Posting
    paginate_by = 30
    info_message = "hello world"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scrapy_settings = settings.SCRAPY
        scrapy_request = f"http://{scrapy_settings['host']:s}:{scrapy_settings['port']:s}/listjobs.json?project=realest_scrap"
        response = get(scrapy_request)
        r_json = response.json()
        if r_json.get('status') == 'ok':
            if len(r_json['pending']) + len(r_json['running']) > 0:
                context["info_message"] = "Crawling in progress, refresh site to load up to date results."
        return context


def request_crawl(request):
    scrapy_settings = settings.SCRAPY
    scrapy_request = f"http://{scrapy_settings['host']:s}:{scrapy_settings['port']:s}/schedule.json"
    category = request.POST["category"]
    api_request_header = {
        'project': 'realest_scrap',
        'spider': 'sreality',
        'posting_category': input_to_category(category).value
    }

    if scrap_limit := request.POST.get("scrap-limit"):
        api_request_header['scrap_limit'] = int(scrap_limit)  # type: ignore
    response = post(scrapy_request, data=api_request_header)
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
