from django.urls import path
from . import views


urlpatterns = [
    path('', views.audit, name='index_audit'),

]