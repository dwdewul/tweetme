from django.conf.urls import url
from .views import (TweetListView, TweetDetailView,
                    TweetCreateView, TweetUpdateView, TweetDeleteView)

urlpatterns = [
    url(r'^$', TweetListView.as_view(), name='list_view'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail_view'),
    url(r'^create/$', TweetCreateView.as_view(), name='create_view'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update_view'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete_view'),
]
