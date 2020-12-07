from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import preconsult


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
    preconsulta = preconsult(name=name, phone=phone, age=age, profession=profession, surgery=surgery,
                             expectancy=expectancy, fear=fear, recommendation=recommendation)
    preconsulta.save()
    return render(request, 'preconsults/preconsultas.html')

