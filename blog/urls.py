from django.conf.urls import url
from django.urls import path
from blog import views


app_name = 'blogTag'

urlpatterns = [

    path('home/', views.home, name='home'),
    path('games/', views.games, name='games'),
    path('review/', views.review, name='review'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('game_single', views.game_single, name='game_single'),
]
