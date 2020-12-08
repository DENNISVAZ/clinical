from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('website.urls')),
    path('usuarios/', include('users.urls')),
    path('permissoes/', include('permissions.urls')),
    path('preconsultas/', include('preconsults.urls')),
    path('satisfacao/', include('satisfaction.urls')),
    path('orcamentos/', include('budgets.urls')),
    path('procedimentos/', include('procedures.urls')),
    path('cirurgias/', include('surgery.urls')),
    path('despesas/', include('expenses.urls')),
    path('auditoria/', include('audit.urls')),
    path('postagens/', include('posts.urls')),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
