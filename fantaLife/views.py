#! /usr/bin/env python3

from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect

from django.views import View




import  sys, os

#home page

def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"Fanta Life",
        # "content":"Graphic design meets engineering",

    }

    return render(request, "home_page.html", context)










































# end
