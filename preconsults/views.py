from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from .models import Preconsult
from django.contrib.auth.decorators import login_required


def preconsults(request):
    if request.method != 'POST':
        return render(request, 'preconsults/preconsultas.html')

    name = request.POST.get('name')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    profession = request.POST.get('profession')
    surgery = request.POST.get('surgery')
    expectancy = request.POST.get('expectancy')
    fear = request.POST.get('fear')
    recommendation = request.POST.get('recommendation')
    if not name or not phone or not age or not profession or not surgery:
        messages.error(request, 'Campos obrigatórios (*)')
        return render(request, 'preconsults/preconsultas.html')
    # rhinoplasty = request.POST.get('name')
    # active = models.BooleanField(default=True)
    # creation_date = models.DateField(default=date.today)
    # creation_time = models.DateTimeField(default=timezone.now)
    preconsulta = Preconsult(name=name, phone=phone, age=age, profession=profession, surgery=surgery,
                             expectancy=expectancy, fear=fear, recommendation=recommendation)
    preconsulta.save()
    messages.success ( request, 'Enviado com sucesso! Agradecemos seu contato.' )
    surgery = request.POST.get('surgery').lower()
    if ('rino' in surgery) or ('nariz' in surgery) or ('rhino' in surgery):
        return render ( request, 'preconsults/enviado.html' )
    else:
        request.POST = []
        return render ( request, 'preconsults/preconsultas.html' )


@login_required(login_url='index')
def listpreconsults(request):
    data = Preconsult.objects.order_by('-creation_time').filter(
        active = True
    )
    return render(request, 'preconsults/list_preconsultas.html', {'dados':data})


@login_required(login_url='index')
def detailpreconsults(request, preconsult_id):
    preconsulta = Preconsult.objects.get(id=preconsult_id)
    return render(request, 'preconsults/detalhe_preconsulta.html', {'preconsulta': preconsulta})

