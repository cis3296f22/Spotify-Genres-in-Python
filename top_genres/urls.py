from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('genres/', views.genre_view, name='genre_view'),
    path('redirect/', views.redirect_view, name='redirect_view')
]
