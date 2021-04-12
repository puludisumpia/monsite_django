from django.urls import path

from . import views

urlpatterns = [
    path("", views.postlist, name="post_list"),
    path("posts/<slug:slug>/", views.postdetail, name="post_detail"),
    path("apropos/", views.apropos, name="apropos"),
    path("contact/", views.contact, name="contact"),
]
