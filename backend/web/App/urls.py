from django.urls import path
from .views import MainWindow, EventCatalog, profile, upload_avatar

urlpatterns = [
    path('', MainWindow.as_view(), name='index'),
    path('catalog/', EventCatalog.as_view(), name='catalog')
]

#Profile
urlpatterns += [
    path('@<str:username>/', profile, name='profile'),
    path('upload_avatar/', upload_avatar, name='upload_avatar' )
]
