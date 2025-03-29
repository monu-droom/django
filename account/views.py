from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print("User:", request.user)
        print("Authenticated:", request.user.is_authenticated)
        if user is not None:
            auth.login(request, user)
            print('Logged in successfully!')
            return redirect('/')
        else:
            messages.info(request, 'Whoops! username or passwrd is wrong')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        #checking for password and confirm password is same
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password1
                )
                if user.save():
                    print('User created successfully.')
        else:
            messages.info(request, 'Whoops! password not matched.')
            return redirect('register')
        return redirect('login')
    else:
        return render(request, 'register.html')
