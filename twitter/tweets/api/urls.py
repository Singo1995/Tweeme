from .views import TweetListAPIView,TweetCreateAPIView,RetweetAPIView,LikeToggleAPIView,TweetDetailAPIView
from  django.urls import path, re_path
from django.views.generic.base import RedirectView
urlpatterns = [
    # path('',RedirectView.as_view(url="/")),
    path('',TweetListAPIView.as_view(),name='list'),
    path('create/',TweetCreateAPIView.as_view(),name='create'),
    re_path(r'(?P<pk>\d+)/retweet/$',RetweetAPIView.as_view(),name='retweet'),
    re_path(r'(?P<pk>\d+)/like/$',LikeToggleAPIView.as_view(),name='like-api'),
    re_path(r'(?P<pk>\d+)/$',TweetDetailAPIView.as_view(),name='detail'),
    # # path('1/',TweetDetailView.as_view(),name='detail'),
    # re_path(r'(?P<pk>\d+)/$',TweetDetailView.as_view(), name='detail'),
    # re_path(r'(?P<pk>\d+)/update/$',TweetUpdateView.as_view(), name='update'),
    # re_path(r'(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(), name='delete'),
]