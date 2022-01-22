from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from blog.forms import UserSignupForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def blog_note(request, id):
    return render(request, 'blog/blog_note.html', {'id': id})


def blog_notes(request):
    return render(request, 'blog/blog_notes.html', {'title': 'Все записи'})


def category_notes(request, cat_id):
    return render(request, 'blog/category_notes.html', {'id': cat_id})


def user_notes(request, user_id):
    return render(request, 'blog/user_notes.html', {'id': user_id})


def current_user_notes(request):
    return render(request, 'blog/current_user_notes.html', {'title': 'Мои записи'})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', context={'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('blog:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserSignupForm()
    return render(request, 'blog/signup.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('blog:login')

