from django.urls import path
from . import views


urlpatterns = [
    path('', views.budgets, name='index_budgets'),

]