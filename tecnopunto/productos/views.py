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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        if paginator and page_obj:
            current = page_obj.number
            total = paginator.num_pages
            start = max(current - 1, 1)
            end = min(start + 2, total)
            start = max(end - 2, 1)
            pages = list(range(start, end + 1))
            context['page_numbers'] = pages
            context['total_pages'] = total
            if pages:
                first = pages[0]
                last = pages[-1]
            else:
                first = last = None
            context['first_page_in_window'] = first
            context['last_page_in_window'] = last
            context['show_first'] = start > 1
            context['show_first_ellipsis'] = first is not None and first > 2
            context['show_last'] = end < total
            context['show_last_ellipsis'] = last is not None and last < total - 1
        return context


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
