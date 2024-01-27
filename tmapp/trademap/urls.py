from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.authenticate, name = "login"),
    path("home", views.load_home, name = "home"),
    path("home/make-a-post", views.make_post, name = "create"),
    path("home/<str:slug>", views.post_details, name = "load"),
]