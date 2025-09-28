from django.contrib import admin
from django.urls import path,include
from productos.views import inicio


urlpatterns = [
   path('admin/', admin.site.urls),
   path('', inicio, name='inicio'), #ruta para la página de inicio
   path('productos/', include('productos.urls')),  # ruta para las vistas de productos
]

