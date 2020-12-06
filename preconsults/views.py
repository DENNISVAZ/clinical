from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def preconsults(request):
    if request.user.is_authenticated:

        messages.add_message ( request, messages.ERROR,
                               '{ request.user.email }' )
        # return render ( request, 'preconsults/preconsultas.html' )
        return redirect ( request.META.get ( "HTTP_REFERER" ) )
    else:
        messages.add_message ( request, messages.ERROR,
                               'Usuário semsd sadf sd acesso a cessa opção!' )
        return redirect ( request.META.get ( "HTTP_REFERER" ))
    endif
