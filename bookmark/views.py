from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookmarkLV(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    model=Bookmark

    # template_name="bookmark/bookmark_list.html" #appname/model_name_list.html
    # context_object_name = "object_list" # object_list
    
class BookmarkDV(DetailView):
    model=Bookmark
     # template_name="bookmark/bookmark_detail.html" #appname/model_name_detail.html
     # context_object_name = "object" # object