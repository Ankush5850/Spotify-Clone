
from django.contrib import admin
from django.urls import path
from .views import RoomView


urlpatterns = [
    # path('home', home)
    path('home', RoomView.as_view())
]
