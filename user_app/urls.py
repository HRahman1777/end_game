from django.urls import path
from user_app import views

app_name = 'user_appTag'

urlpatterns = [

    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]
