from django.shortcuts import render,redirect, get_object_or_404
from .models import User
from .forms import UserForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = UserForm(request.POST)
        new_id = get_object_or_404(User, username=request.POST['username'])
        if register_form.is_valid():
            if new_id:
                error_message = '이미 존재하는 이름입니다.'
                return render(request, 'register.html', {'register_form':register_form, 'error_message':error_message})
            else:
                register_form.save()
                return redirect('posts:list')
    else:
        register_form = UserForm()

    return render(request, 'register.html', {'register_form':register_form})

def save_session(request, user_id, user_pw):
    request.session['user_id'] = user_id
    request.session['user_pw'] = user_pw

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        user_id = request.POST['username']
        user_pw = request.POST['password']

        if login_form.is_valid():
            request.session['user'] = login_form.user_id
            save_session(request, user_id, user_pw)
            return redirect('posts:list')
    else:
        login_form = LoginForm()

    return render(request, 'login.html', {'login_form':login_form})

def logout(request):
    if request.session.get('user'):
        del(request.session['user'], request.session['user_id'], request.session['user_pw'])
    return redirect('posts:list')