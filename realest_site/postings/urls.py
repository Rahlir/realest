from django.urls import path

from postings.views import IndexView, PostingDetailView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', PostingDetailView.as_view(), name='detail'),
]
