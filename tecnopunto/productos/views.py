from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from .forms import ProductoForm
from .models import Producto


class InicioView(TemplateView):
    template_name = 'inicio.html'


class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/product_list.html'
    context_object_name = 'productos'
    paginate_by = 10
    ordering = ['-fecha_ultima_modificacion']


class BaseProductoFormView:
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/product_form.html'
    success_url = reverse_lazy('productos:list')

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class ProductoCreateView(BaseProductoFormView, CreateView):
    success_message = 'Producto creado correctamente.'


class ProductoUpdateView(BaseProductoFormView, UpdateView):
    success_message = 'Producto actualizado correctamente.'


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/product_confirm_delete.html'
    success_url = reverse_lazy('productos:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Producto eliminado correctamente.')
        return super().delete(request, *args, **kwargs)
