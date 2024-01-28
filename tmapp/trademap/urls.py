from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path('login/', views.user_login, name = "login"),
    path('signup/', views.user_signup, name = "signup"),
    path('logout/', views.user_signup, name = "logout"),
    path("make-a-post/", views.make_post, name = "create"),
    path("<str:slug>/", views.post_details, name = "load"),
]