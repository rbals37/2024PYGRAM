from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')

        user = authenticate(request, student_id=student_id, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('main')
        else:
            messages.error(request, '잘못된 학번 또는 비밀번호입니다.')
    return render(request, 'login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('main') 