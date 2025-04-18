from django.urls import path

from .views import AuthenticationView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', AuthenticationView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]