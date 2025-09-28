from django.contrib import admin
from django.urls import include, path

from productos.views import InicioView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name='inicio'),
    path('productos/', include('productos.urls')),
]
