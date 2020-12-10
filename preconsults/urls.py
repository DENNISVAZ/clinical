from django.urls import path
from . import views


urlpatterns = [
    path('', views.preconsults, name='index_preconsults'),
    path('listagem', views.listpreconsults, name='list_preconsults'),
    path('enviado', views.send, name='send_preconsults'),
    path('<int:preconsult_id>', views.detailpreconsults, name='detail_preconsults')

]