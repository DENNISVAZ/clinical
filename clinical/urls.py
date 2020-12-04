from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('website.urls')),
    path('usuarios/', include('users.urls')),
    path('admin/', admin.site.urls),
]
