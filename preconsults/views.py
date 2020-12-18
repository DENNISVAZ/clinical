from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.template.loader import get_template

from .models import Preconsult
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from django.utils.dateformat import DateFormat
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.generic.base import View
import xhtml2pdf.pisa as pisa
from django.http import HttpResponse
import io


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
    if ('rino' in surgery.lower()) or ('nariz' in surgery.lower()) or ('rhino' in surgery.lower()):
        preconsulta.rhinoplasty = True
    else:
        preconsulta.rhinoplasty = False
    preconsulta.save()
    messages.success ( request, 'Enviado com sucesso! Agradecemos seu contato.' )
    surgery = request.POST.get('surgery').lower()
    if preconsulta.rhinoplasty:
        return render (request, 'preconsults/enviado.html' )
    else:
        request.POST = []
        return render ( request, 'preconsults/preconsultas.html' )


@login_required(login_url='index')
def listpreconsults(request):
    if request.method != 'POST':
        # page = request.GET.get('pg')
        first_date = request.GET.get('first_date', date.today () - timedelta ( days=1 ))
        last_date = request.GET.get('last_date', date.today ())
        first_date = DateFormat ( first_date ).format ( 'yy-m-d' )
        last_date = DateFormat ( last_date ).format ( 'yy-m-d' )
        search = ""
    else:
        first_date = request.POST.get('first_date')
        last_date = request.POST.get('last_date')
        search = request.POST.get ( 'search' )
        page = request.GET.get('pg')
    if first_date > last_date:
        messages.error(request, 'Data Inicial deve ser anterior a data Final.')
    data = Preconsult.objects.order_by('-creation_time').filter(
        Q(name__icontains=search)|Q(phone__icontains=search)|Q(profession__icontains=search)|Q(surgery__icontains=search),
        creation_date__lte = last_date,
        creation_date__gte = first_date,
        active = True
    )
    if not data:
        messages.error(request, 'Dados não encontrados para esse período e pesquisa.')
    # paginator = Paginator(data, 5)
    # data = paginator.get_page(page)

    return render(request, 'preconsults/list_preconsultas.html', {'dados': data,
                                                                  'first_date': first_date,
                                                                  'last_date': last_date,
                                                                  'search' : search,
                                                                  })


@login_required(login_url='index')
def detailpreconsults(request, preconsult_id):
    # if request.method != 'POST':
    #     delete = False
    # else:
    #     rinoplastia = request.POST.get('rino')
    #
    #     if rinoplastia == 'on':
    #         rinoplastia = True
    #     else:
    #         rinoplastia = False
    #     preconsulta = Preconsult(rhinoplasty=rinoplastia)
    #     preconsulta.save()
    #     messages.success(request, rinoplastia)
    preconsulta = Preconsult.objects.get(id=preconsult_id)


    return render(request, 'preconsults/detalhe_preconsulta.html', {'preconsulta': preconsulta,
                                                                    })
    #

def send(request):
    if request.method == 'POST':
        prec = Preconsult.objects.last()
        preconsulta = Preconsult.objects.get(id=prec.id)
        preconsulta.checklink = True
        preconsulta.save()
        return redirect('https://my.crisalix.com/signup/drcurado')
    preconsulta = Preconsult.objects.last()


    return render(request, 'preconsults/enviado.html', {'preconsulta': preconsulta })

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response, encoding='UTF-8'
        )
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf'
            )
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error para gerar PDF", status=400)




def printdetail(request, preconsult_id):
    preconsulta = Preconsult.objects.get(id=preconsult_id)
    preconsulta.surgery.encode('ascii', 'ignore').decode('ascii')
    params = {
        'dados': preconsulta,
        'request': request,
    }
    if len(str(preconsulta.name).split()) > 1:
        file_name = str(preconsulta.name).split()[0]+str(preconsulta.name).split()[1]
    else:
        file_name = str(preconsulta.name).split()[0]
    return Render.render('preconsults/print_relatorio.html', params, file_name)