from django.urls import path

from .views import (
    InicioView,
    ProductoCreateView,
    ProductoDeleteView,
    ProductoListView,
    ProductoUpdateView,
)

app_name = 'productos'

urlpatterns = [
    path('', ProductoListView.as_view(), name='list'),
    path('nuevo/', ProductoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', ProductoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', ProductoDeleteView.as_view(), name='delete'),
    path('inicio/', InicioView.as_view(), name='inicio'),
]
