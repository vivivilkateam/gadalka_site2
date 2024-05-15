from django.urls import include, path

from . import views

urlpatterns = [
    path('info/', views.index),
    path('about/', views.about),
    path('', views.glava)
]
