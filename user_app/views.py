from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if user_name=='' or password1=='':
            messages.info(request, "At least enter username and password")
            return redirect('user_appTag:signup')
        else:
            if password1 == password2:
                if User.objects.filter(username=user_name).exists():
                    messages.info(request, "username already taken")
                    return redirect('user_appTag:signup')
                else:
                    user = User.objects.create_user(username=user_name, password=password1, email=email,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('home')
            else:
                messages.info(request, "Password Not matched!")
                return redirect('user_appTag:signup')

    else:
        return render(request, 'blog/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info( request,"wrong username/password !")
            return redirect('user_appTag:login')
    return render(request, 'blog/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
