from django.conf.urls import url
from .views import tweet_list_view, tweet_detail_view

urlpatterns = [
    url(r'^$', tweet_list_view, name='list_view'),
    url(r'^1/$', tweet_list_view, name='detail_view'),
]
