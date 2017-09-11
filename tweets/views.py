from django.shortcuts import render
from django.urls import reverse_lazy
from django.forms.utils import ErrorList
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import (DetailView, ListView,
                                  CreateView, UpdateView, DeleteView)
from .forms import TweetModelForm
from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetListView(ListView):
    template_name = "tweets/list_view.html"
    context_object_name = 'tweets'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(text__icontains=query) |
            Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweets:create_view")
        return context


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"
    context_object_name = 'tweet'


class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = "tweets/update.html"
    login_url = '/admin/login/'
    success_url = reverse_lazy("tweets:list_view")


class TweetUpdateView(UserOwnerMixin, UpdateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = "tweets/update.html"
    login_url = '/admin/login/'
    success_url = reverse_lazy("tweets:list_view")


class TweetDeleteView(LoginRequiredMixin, UserOwnerMixin, DeleteView):
    model = Tweet
    template_name = "tweets/delete.html"
    success_url = reverse_lazy("tweets:list_view")
    login_url = '/admin/login/'
