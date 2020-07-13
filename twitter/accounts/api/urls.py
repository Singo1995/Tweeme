from tweets.api.views import TweetListAPIView,LikeToggleAPIView
from  django.urls import path, re_path, include
from django.views.generic.base import RedirectView
urlpatterns = [
    # path('',RedirectView.as_view(url="/")),
    # re_path(r'(?P<username>[\w.@+-]+)/like/$',LikeToggleAPIView.as_view(),name='like-api'),
    re_path(r'(?P<username>[\w.@+-]+)/tweet/$',TweetListAPIView.as_view(),name='list-api'),
    path('', include('django.contrib.auth.urls')),
]