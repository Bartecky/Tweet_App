from django.contrib.auth.mixins import LoginRequiredMixin
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


# Create your views here.
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

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
