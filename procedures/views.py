from django.shortcuts import render


def procedures(request):
    return render(request, 'procedures/procedimentos.html')
