"""twitter_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import (
    UserDetailView,
    UserFollowView
)

urlpatterns = [
    # url(r'^$', RedirectView.as_view(url='/')),
    # url(r'^search/$', TweetListView.as_view(), name='tweet-list'),
    # url(r'^create/$', TweetCreateView.as_view(), name='tweet-create'),
    url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name='user-follow'),
    # url(r'^(?P<pk>(\d)+)/update/$', TweetUpdateView.as_view(), name='tweet-update'),
    # url(r'^(?P<pk>(\d)+)/delete/$', TweetDeleteView.as_view(), name='tweet-delete'),

]
