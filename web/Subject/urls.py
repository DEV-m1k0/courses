from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

form = RegistrationForm()

#Auth
urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('', include('authentication.urls'))
]

#Password_Reset
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
