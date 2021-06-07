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
import datetime
from django.http import HttpResponse
import io


def preconsults(request):
    mes_atual = date.today().month; ano_atual = date.today().year;
    mes1 = str(mes_atual).zfill(2) +'/'+ str(ano_atual)
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes2 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes3 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes4 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes5 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes6 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes7 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes8 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes9 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes10 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes11 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    mes_atual = mes_atual + 1;
    if mes_atual > 12:
        mes_atual = 1
        ano_atual = ano_atual + 1
    mes12 = str ( mes_atual ).zfill ( 2 ) + '/' + str ( ano_atual )
    params = {
        'mes1': mes1,
        'mes2': mes2,
        'mes3': mes3,
        'mes4': mes4,
        'mes5': mes5,
        'mes6': mes6,
        'mes7': mes7,
        'mes8': mes8,
        'mes9': mes9,
        'mes10': mes10,
        'mes11': mes11,
        'mes12': mes12,
    }
    if request.method != 'POST':
        check_prosthesis = False
        check_mastopexy = False
        check_liposculpture = False
        check_abdominoplasty = False
        check_lifting = False
        check_rinoplasty = False
        check_otoplasty = False
        check_nymphoplasty = False

        return render(request, 'preconsults/preconsultas.html', params)
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    age = request.POST.get('age')
    profession = request.POST.get('profession')
    surgery = request.POST.get('surgery')
    height = request.POST.get('height')
    weight = request.POST.get('weight')
    expectancy = request.POST.get('expectancy')
    fear = request.POST.get('fear')
    recommendation = request.POST.get('recommendation')
    check_prosthesis = request.POST.get('check_prosthesis', False)
    check_mastopexy = request.POST.get('check_mastopexy', False)
    check_liposculpture = request.POST.get('check_liposculpture', False)
    check_abdominoplasty = request.POST.get('check_abdominoplasty', False)
    check_rinoplasty = request.POST.get ( 'check_rinoplasty' , False)
    check_lifting = request.POST.get('check_lifting', False)
    check_otoplasty = request.POST.get('check_otoplasty', False)
    check_nymphoplasty = request.POST.get('check_nymphoplasty', False)
    date_operate = request.POST.get('date_operate', '')
    if not name \
            or not phone \
            or not age \
            or not height \
            or not weight \
            or date_operate == 'Selecione'\
            or not profession \
            or (not check_prosthesis and not surgery and not check_mastopexy
                and not check_liposculpture
                and not check_abdominoplasty and not check_lifting and not check_rinoplasty
                and not check_otoplasty and not check_nymphoplasty):
        messages.error(request, 'Campos obrigatórios (*)')
        return render(request, 'preconsults/preconsultas.html', params)
    # rhinoplasty = request.POST.get('name')
    # active = models.BooleanField(default=True)
    # creation_date = models.DateField(default=date.today)
    # creation_time = models.DateTimeField(default=timezone.now)
    if check_prosthesis == 'on':
        check_prosthesis = True
    else:
        check_prosthesis = False
    if check_mastopexy == 'on':
        check_mastopexy = True
    else:
        check_mastopexy = False
    if check_liposculpture == 'on':
        check_liposculpture = True
    else:
        check_liposculpture = False
    if check_abdominoplasty == 'on':
        check_abdominoplasty = True
    else:
        check_abdominoplasty = False
    if check_lifting == 'on':
        check_lifting = True
    else:
        check_lifting = False
    if check_rinoplasty == 'on':
        check_rinoplasty = True
    else:
        check_rinoplasty = False
    if check_otoplasty == 'on':
        check_otoplasty = True
    else:
        check_otoplasty = False
    if check_nymphoplasty == 'on':
        check_nymphoplasty = True
    else:
        check_nymphoplasty = False
    preconsulta = Preconsult(name=name, phone=phone, age=age, height=height, weight=weight,
                             profession=profession, surgery=surgery,
                             expectancy=expectancy, fear=fear, recommendation=recommendation,
                             check_prosthesis=check_prosthesis,
                             check_mastopexy=check_mastopexy,
                             check_liposculpture=check_liposculpture,
                             check_abdominoplasty=check_abdominoplasty,
                             check_lifting=check_lifting,
                             check_rinoplasty=check_rinoplasty,
                             check_otoplasty=check_otoplasty,
                             check_nymphoplasty=check_nymphoplasty,
                             date_operate=date_operate)
    if ('rino' in surgery.lower()) or ('nariz' in surgery.lower()) or ('rhino' in surgery.lower()) or (check_rinoplasty):
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
        return render ( request, 'preconsults/preconsultas.html' , params)


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
    phone_str = 'TELEFONE'.ljust(40)
    age_str = 'IDADE'.ljust(15)
    height_str = 'ALTURA'.ljust(15)
    weight_str = 'PESO'.ljust(15)
    preconsulta = Preconsult.objects.get(id=preconsult_id)
    preconsulta.name = preconsulta.name.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.phone = preconsulta.phone.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.phone = preconsulta.phone.ljust(40)
    preconsulta.age = preconsulta.age.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.age = preconsulta.age.ljust(15)
    preconsulta.height = preconsulta.height.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.height = preconsulta.height.ljust(15)
    preconsulta.weight = preconsulta.weight.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.weight = preconsulta.weight.ljust(15)
    preconsulta.profession = preconsulta.profession.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.surgery = preconsulta.surgery.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.expectancy = preconsulta.expectancy.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.fear = preconsulta.fear.encode('ascii', 'ignore').decode('utf-8')
    preconsulta.recommendation = preconsulta.recommendation.encode('ascii', 'ignore').decode('utf-8')
    params = {
        'dados': preconsulta,
        'request': request,
        'phone_str': phone_str,
        'age_str': age_str,
        'height_str': height_str,
        'weight_str': weight_str
    }
    if len(str(preconsulta.name).split()) > 1:
        file_name = str(preconsulta.name).split()[0]+str(preconsulta.name).split()[1]
    else:
        file_name = str(preconsulta.name).split()[0]
    return Render.render('preconsults/print_relatorio.html', params, file_name)