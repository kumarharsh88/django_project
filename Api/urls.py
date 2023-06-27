from django.contrib import admin
from django.urls import path
from .views import UserView,BlogView

urlpatterns = [
    path("user",UserView.as_view(),name="user"),
    path("blog/<int:id>",BlogView.as_view(),name="blog")
]
