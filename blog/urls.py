from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),             
    path("blogs/", views.post_list, name="post_list"),
    path("blogs/create/", views.post_create, name="post_create"),
    path("blogs/<int:pk>/update/", views.post_update, name="post_update"),
    path("blogs/<int:pk>/delete/", views.post_delete, name="post_delete"),
]
