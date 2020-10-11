from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<str:category>", views.category, name="category"),
    path("allnews", views.allnews, name="allnews"),
    path("contact", views.contact, name="contact"),
]