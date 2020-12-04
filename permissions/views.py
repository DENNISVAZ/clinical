from django.shortcuts import render


def permissions(request):
    return render(request, 'permissions/permissoes.html')
