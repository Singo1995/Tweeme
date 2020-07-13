from rest_framework import generics,permissions
from django.db.models import Q
from tweets.models import Tweet
from .serializers import TweetModelSerializer
from rest_framework.views import APIView 
from rest_framework.response import Response
from .pagination import StandardResultsPagination



class LikeToggleAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print("LikeToggleAPIView")
    def get(self,request,pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        print(tweet_qs)
        message = "Not allowed"
        if request.user.is_authenticated:
            print("Reaching here")
            is_liked = Tweet.objects.like_toggle(request.user, tweet_qs.first())
            print(is_liked)
            #data= TweetModelSerializer(is_liked).data
            return Response({"liked":is_liked})
        return Response({"message":message}, status=400)

class RetweetAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        #print(tweet_qs.user)
        message = "Not allowed"
        if tweet_qs.exists() and tweet_qs.count() == 1:
            if request.user.is_authenticated:
                new_tweet = Tweet.objects.retweet(request.user, tweet_qs.first())
            if new_tweet is not None:
                data= TweetModelSerializer(new_tweet).data
                return Response(data)
            message = "Cannot Retweet the same in 1 day"
        return Response({"message":message}, status=400)

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class TweetDetailAPIView(generics.RetrieveAPIView):
    queryset = Tweet.objects.all()
    pagination_class = StandardResultsPagination
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self,*args,**kwargs):
        tweet_id = self.kwargs.get("pk")
        qs = Tweet.objects.filter(pk = tweet_id)
        return qs


class SearchTweetAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all().order_by("-timestamp")
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(SearchTweetAPIView, self).get_serializer_context(*args, **kwargs)
        context['request'] = self.request
        return context

    def get_queryset(self, *args, **kwargs):
        qs = self.queryset
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs
class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self, *args, **kwargs):
        context = super(TweetListAPIView, self).get_serializer_context(*args,**kwargs)
        context["request"]= self.request
        return context

    def get_queryset(self, *args,**kwargs):
        requested_user = self.kwargs.get("username")
        if requested_user:
            qs = Tweet.objects.filter(user__username=requested_user).order_by('-timestamp')
        else:
            im_following= self.request.user.profiles.get_following()
            qs1 = Tweet.objects.filter(user__in=im_following)
            qs2 = Tweet.objects.filter(user=self.request.user)
            qs  = (qs1 | qs2).distinct().order_by('-timestamp')
            print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(Q(content__icontains= query) | Q(user__username__icontains=query))
                        
        return qs