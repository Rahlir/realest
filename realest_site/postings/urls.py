from django.urls import path

from postings.views import IndexView, PostingDetailView, request_crawl


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PostingDetailView.as_view(), name='detail'),
    path('crawl/', request_crawl, name='crawl'),
]
