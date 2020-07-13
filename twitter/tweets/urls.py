from .views import *
from  django.urls import path, re_path, include
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',RedirectView.as_view(url="/")),
    path('search/',TweetListView.as_view(),name='list'),
    path('create/',TweetFormView.as_view(),name='create'),
    # path('1/',TweetDetailView.as_view(),name='detail'),
    re_path(r'(?P<pk>\d+)/$',TweetDetailView.as_view(), name='detail'),
    re_path(r'(?P<pk>\d+)/retweet/$',RetweetView.as_view(), name='retweet'),
    re_path(r'(?P<pk>\d+)/update/$',TweetUpdateView.as_view(), name='update'),
    re_path(r'(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(), name='delete'),
    path('', include('django.contrib.auth.urls')),
]