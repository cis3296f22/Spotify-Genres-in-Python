from django.urls import path
from . import views

urlpatterns = [
    #path('', views.login_view, name='login_view'),
    path('', views.top_genre_view, name='top_genre_view'),
]
