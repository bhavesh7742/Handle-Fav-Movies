from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('create/', views.movie_create, name='movie_create'),
    path('edit/<int:movie_id>/', views.movie_edit, name='movie_edit'),
    path('delete/<int:movie_id>/', views.movie_delete, name='movie_delete'),

    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
]
