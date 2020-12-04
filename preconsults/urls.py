from django.urls import path
from . import views


urlpatterns = [
    path('', views.preconsults, name='index_preconsults'),

]