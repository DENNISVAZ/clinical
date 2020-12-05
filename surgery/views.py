from django.shortcuts import render


def surgery(request):
    return render(request, 'surgery/cirurgias.html')
