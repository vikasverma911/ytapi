from django.contrib import admin
from django.urls import path

from searchapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.YoutubeItems.as_view())
]