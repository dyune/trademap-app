from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "home"),
    path("make-a-post/", views.make_post, name = "create"),
    path("input", views.input_form, name = "input"),
    path("output_test/", views.output_values, name = "output_values"),
    path("<str:slug>/", views.post_details, name = "load"),
]