from django.shortcuts import render
from .models import Tweet
# Create your views here.

def tweet_list_view(request):
    tweets = Tweet.objects.all()
    return render(request, "tweets/list_view.html", {'tweets': tweets})

def tweet_detail_view(request, id=1):
    tweet = Tweet.objects.filter(id=id)
    return render(request, "tweets/detail_view.html", {'tweet': tweet})
