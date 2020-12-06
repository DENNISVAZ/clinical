from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User


def index(request):
    user = request.user

    return render(request, 'website/index.html')
