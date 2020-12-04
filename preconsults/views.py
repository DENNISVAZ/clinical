from django.shortcuts import render


def preconsults(request):
    return render(request, 'preconsults/preconsultas.html')
