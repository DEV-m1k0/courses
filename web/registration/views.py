from django.shortcuts import render
from django.views import generic

from .forms import RegistrationForm
from Subject.models import User

# Create your views here.

class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    model = User
    template_name = 'registration/registration.html'