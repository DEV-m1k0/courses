# ---------------------------------- Imports --------------------------------- #

from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from django.views import generic
from django.views.generic.base import ContextMixin

import requests, json

from .forms import MyAuthForm
from Subject.models import User
from .logic.jwt_tokens import JwtTokens

# ------------------------------- Classes View ------------------------------- #

class AuthenticationView(generic.FormView):
    """
    Authorization of the user in the system
    """
    form_class = MyAuthForm
    template_name = 'authentication/auth.html'
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registered = self.request.GET.get("registered", False) == 'True'
        if registered:
            context['registered'] = True
        return context
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        username: str = request.POST['username']
        password: str = request.POST['password']

        jwt = JwtTokens(request=request)
        jwt.login(username, password)

        return super().post(request, *args, **kwargs)
    
