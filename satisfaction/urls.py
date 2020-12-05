from django.urls import path
from . import views


urlpatterns = [
    path('', views.satisfaction, name='index_satisfaction'),

]