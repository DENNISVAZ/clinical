from django.shortcuts import render


def audit(request):
    return render(request, 'audit/auditoria.html')
