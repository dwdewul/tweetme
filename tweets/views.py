from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from .forms import TweetModelForm
from .models import Tweet


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = "tweets/list_view.html"
    context_object_name = 'tweets'


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"
    context_object_name = 'tweet'


class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetModelForm
    # fields = ['user', 'text']
    template_name = "tweets/create.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)
