from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from blog.models import UserInfo, account


# Create your views here.
def home(request):
    count = User.objects.count()
    dict = account.objects.all()
#    user1 = UserInfo()
#    user1.name='Hasibur'
#    user1.email='hasibur@gmail.com'
#    user1.image = 'author.jpg'
 #   dict = [user1, user2]

    return render(request, 'blog/home.html', {'dict':dict, 'count': count})

def games(request):
    return render(request, 'blog/games.html')

def review(request):
    return render(request, 'blog/review.html')

def blog(request):
    return render(request, 'blog/blog.html')

def contact(request):
    return render(request, 'blog/contact.html')

def game_single(request):
    return render(request, 'blog/game-single.html')
