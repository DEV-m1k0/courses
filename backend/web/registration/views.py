from django.shortcuts import render, redirect
from django.views import generic

from .forms import RegistrationForm
from Subject.models import User

# Create your views here.

class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'registration/registration.html'
    success_url = "/login/"

    def post(self, request, *args, **kwargs):
        # return super().post(request, *args, **kwargs)
        return redirect("/login/?registered=True")