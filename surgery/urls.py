from django.urls import path
from . import views


urlpatterns = [
    path('', views.surgery, name='index_surgery'),

]