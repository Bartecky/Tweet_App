from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import (
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet, pk=pk)
        if request.user.is_authenticated:
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect('/')
        return HttpResponseRedirect(tweet.get_absolute_url())


class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'twitter_app/tweet_create.html'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = 'twitter_app/tweet_update.html'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'twitter_app/tweet_delete.html'
    success_url = reverse_lazy('tweet:tweet-list')


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'twitter_app/tweet_list.html'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:tweet-create")
        return context
