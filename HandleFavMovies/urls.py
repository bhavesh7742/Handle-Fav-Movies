"""
URL configuration for HandleFavMovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('movie_list'), name='home'),
    path('movie/', include('movie.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
