from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

from .views import AuthenticationView


urlpatterns = [
    path('login/', AuthenticationView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]

urlpatterns += [
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),
         name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(),
          name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),
         name ='password_reset_complete'),
]