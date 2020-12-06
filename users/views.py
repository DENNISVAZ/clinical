from django.shortcuts import render, redirect
from django.contrib import auth, messages


def login(request):
    if request.method != 'POST':
        return redirect(request.META.get("HTTP_REFERER"))
    user = request.POST.get('user')
    password = request.POST.get('password')
    user = auth.authenticate(request, username=user, password=password)
    if not user:
        messages.error(request,'Usuário ou senha inválidos')
        return redirect(request.META.get("HTTP_REFERER"))
    else:
        auth.login(request,user)
        messages.success(request,'Login realizado com sucesso!')
        return redirect('index')



def logout(request):
    auth.logout(request)
    print('aqui')
    return redirect('index')


