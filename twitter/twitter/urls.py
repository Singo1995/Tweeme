"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include,re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *
from tweets.api.views import SearchTweetAPIView
from tweets.views import TweetListView
from hashtags.views import HashTagView
from hashtags.api.views import TagTweetAPIView
from accounts.views import UserRegisterView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TweetListView.as_view(),name='home'),
    path('search/', SearchView.as_view(),name='search'),
    path('register/', UserRegisterView.as_view(),name='register'),
    path('profiles/', include(('accounts.urls','accounts'), namespace = 'profiles')),
    path('tweet/', include(('tweets.urls','tweets'), namespace = 'tweet')),
    path('api/tweet/', include(('tweets.api.urls','tweets'), namespace = 'tweet-api')),
    path('api/search/',SearchTweetAPIView.as_view(), name= 'search-api'),
    re_path('api/tags/(?P<hashtag>.*)/$',TagTweetAPIView.as_view(), name= 'tag-api'),
    path('api/', include(('accounts.api.urls','accounts'), namespace = 'profiles-api')),
    re_path('tags/(?P<hashtag>.*)/$', HashTagView.as_view(), name= 'hashtag'),
    path('', include('django.contrib.auth.urls')),
]


urlpatterns += staticfiles_urlpatterns()