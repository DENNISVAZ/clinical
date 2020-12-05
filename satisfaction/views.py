from django.shortcuts import render


def satisfaction(request):
    return render(request, 'satisfaction/satisfacao.html')

