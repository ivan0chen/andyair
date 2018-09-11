from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

from account.forms import UserForm, LoginForm
from account.models import User

def userCreate(request, template_name='account/register.html'):
    userForm = UserForm(request.POST or None)
    if userForm.is_valid():
        userForm.save(commit=True)
        messages.success(request, '歡迎註冊!')
        username = userForm.cleaned_data.get('username')
        password = userForm.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        messages.success(request, '登入成功！')
        return redirect('main:main')
    ctx = {}
    ctx['userForm'] = userForm
    ctx['title'] = 'New'
    return render(request, template_name, ctx)

@login_required
def userUpdate(request, pk, template_name='account/register.html'):
    user = get_object_or_404(User, pk=pk)
    userForm = UserForm(request.POST or None, instance=user)
    ctx ={}
    if userForm.is_valid():
        userForm.save(commit=True)
        messages.success(request, '用戶資料已更新！')
        username = userForm.cleaned_data.get('username')
        password = userForm.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return redirect('account:userUpdate', user.id)
    ctx['userForm'] = userForm
    return render(request, template_name, ctx)

def login(request, template_name='account/login.html'):
    form = LoginForm(request.POST or None)
    ctx ={}
    if request.method == 'POST' and request.is_ajax():
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        user = authenticate(username=username, password=password)
        result = 'Failure'
        if user and user.is_active:
            #login success
            auth_login(request, user)
            nextURL = request.POST.get('nextURL')
            if nextURL:
                return redirect(nextURL)
            messages.success(request, '登入成功！')
            result = 'Success'
            # return redirect('main:main')
        else:
            messages.warning(request, '登入失敗!')

        django_messages = []
        for message in messages.get_messages(request):
            django_messages.append({
                "level": message.level,
                "message": message.message,
                "tags": message.tags,
            })

        ctx['request'] = request.POST
        ctx['result'] = result
        ctx['messages'] = django_messages
        print(ctx)
        return JsonResponse(ctx)

    ctx['form'] = form
    ctx['nextURL'] = request.GET.get('next')
    print(ctx)
    return render(request, template_name, ctx)

@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, '登出成功！')
    return redirect('main:main')

