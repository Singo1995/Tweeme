from .views import UserDetailView,UserFollowView
from  django.urls import path, re_path
from django.views.generic.base import RedirectView
urlpatterns = [
    # path('',RedirectView.as_view(url="/")),
    # path('',TweetListAPIView.as_view(),name='list'),
    # path('create/',TweetCreateAPIView.as_view(),name='create'),
    # # path('1/',TweetDetailView.as_view(),name='detail'),
    re_path(r'(?P<username>[\w.@+-]+)/follow/$',UserFollowView.as_view(), name='follow'),
    re_path(r'(?P<username>[\w.@+-]+)/$',UserDetailView.as_view(), name='userdetail'),
    
    # re_path(r'(?P<pk>\d+)/update/$',TweetUpdateView.as_view(), name='update'),
    # re_path(r'(?P<pk>\d+)/delete/$',TweetDeleteView.as_view(), name='delete'),
]