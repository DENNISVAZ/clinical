from django.urls import path
from . import views


urlpatterns = [
    path('', views.procedures, name='index_procedures'),

]