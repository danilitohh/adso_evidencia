from django.urls import path
from . import views  # Importamos las vistas de la aplicación productos


app_name = 'productos'
urlpatterns = [
   path('', views.lista_productos, name='lista'),
   path('nuevo/', views.create_product, name='nuevo'),
   path('editar/<int:pk>/', views.edit_product, name='editar'),
   path('eliminar/<int:pk>/', views.delete_product, name='eliminar'),
]
