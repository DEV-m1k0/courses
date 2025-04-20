from django.contrib import admin
from django.urls import path, include

#Administrations
urlpatterns = [
    path('admin/', admin.site.urls),
]

#includes
urlpatterns += [
    path("", include("registration.urls")),
    path('', include('authentication.urls')),
    path('',include('App.urls')),
    path('',include('Event.urls')),
    path('api/',include('api.urls')),
]