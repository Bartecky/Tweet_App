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
from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from twitter_app.views import TweetListView
from hashtags.views import HashTagView


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='home'),
    url(r'^tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name='hashtag'),
    url(r'^tweet/', include(('twitter_app.urls', 'tweet'), namespace='tweet')),
    url(r'^api/tweet/', include(('twitter_app.api.urls', 'tweet-api'), namespace='tweet-api')),
    url(r'^api/', include(('accounts.api.urls', 'accounts-api'), namespace='accounts-api')),
    url(r'^', include(('accounts.urls', 'profiles'), namespace='profiles')),

]

if settings.DEBUG:
    urlpatterns += (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))