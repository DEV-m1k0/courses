from django.urls import path
from api.user.get.views import UsernameListAPIView

urlpatterns = [
    path('users', UsernameListAPIView.as_view()),
]