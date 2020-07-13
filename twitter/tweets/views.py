from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tweet
from .forms import TweetModelForm
from django.views.generic import DetailView,ListView,FormView,CreateView,UpdateView,DeleteView
from .mixins import FormUserNeededMixin,UserOwnerMixin
from django.urls import reverse_lazy
from django.http import request, HttpResponseRedirect
from django.db.models import Q
from django.views import View
#from django.views.generic.edit import DeleteView
# Create your views here.


class TweetFormView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    print("1")
    form_class = TweetModelForm
    template_name = 'tweets/create_view.html'
    # success_url = "/tweet/create/"
    # success_url =reverse_lazy("tweet:detail")
    # login_url = "/admin/"
    
# class AuthorCreate(CreateView):
#     model = Author
#     fields = ['name']
class RetweetView(View):
    def get(self, request, pk, *args, **kwargs):
        tweet = get_object_or_404(Tweet,pk=pk)
        if request.user.is_authenticated:
            print(Tweet.objects)
            new_tweet = Tweet.objects.retweet(request.user, tweet)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect("/")

class TweetDetailView(DetailView):
    # template_name = "tweets/tweet_detail.html"
    queryset = Tweet.objects.all()

    # def get_object(self):
    #     print(self.kwargs)
    #     pk = self.kwargs.get("pk")
    #     return Tweet.objects.get(id = pk)

class TweetListView(LoginRequiredMixin,ListView):
    def get_queryset(self, *args,**kwargs):
        qs = Tweet.objects.all()
        # print(self.request.GET)
        query = self.request.GET.get("q",None)
        if query is not None:
            qs = qs.filter(Q(content__icontains= query) | Q(user__username__icontains=query))
                          
        return qs
         
    template_name = "tweets/tweet_list.html"
    # queryset = Tweet.objects.all()

    def get_context_data(self,*args,**kwargs):
        context = super(TweetListView,self).get_context_data(*args,**kwargs)
        
        context['create_form'] = TweetModelForm
        context['create_url'] = reverse_lazy("tweet:create")
        print(context)
        return context

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/update_view.html"
    # success_url = "/tweet/"

class TweetDeleteView(LoginRequiredMixin,DeleteView):
    #print("Reaching Here")
    model = Tweet
    template_name = "tweets/delete_view.html"
    success_url = reverse_lazy("tweet:list")
    # success_url = reverse_lazy('home')
# def tweet_detail_view(request,id=3):
#     obj = Tweet.objects.get(id = id)
#     print(obj)
#     context = {
#         "object": obj,
#         "abc": obj,
#     }
#     return render(request, "tweets/detail_view.html", context)

# def tweet_list_view(request,id=1):
#     queryset = Tweet.objects.all()
#     for obj in queryset:
#         print(obj.content)
#     context = {
#         "object_list": queryset
#     }
#     return render(request, "tweets/list_view.html", context)
