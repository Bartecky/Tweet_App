from django.views.generic import DetailView, ListView, CreateView
from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin


# Create your views here.
class TweetCreateView(FormUserNeededMixin, CreateView):
    form_class = TweetModelForm
    template_name = 'twitter_app/tweet_create.html'
    success_url = '/tweet/'


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()


class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'twitter_app/tweet_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
