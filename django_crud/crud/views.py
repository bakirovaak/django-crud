from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import ItemForm
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'crud/item_list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(title__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['q'] = self.request.GET.get('q', '')
        return ctx


class ItemDetailView(DetailView):
    model = Item
    template_name = 'crud/item_detail.html'


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'crud/item_form.html'
    success_url = reverse_lazy('crud:list')

    def form_valid(self, form):
        messages.success(self.request, 'Запись создана')
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'crud/item_form.html'
    success_url = reverse_lazy('crud:list')

    def form_valid(self, form):
        messages.success(self.request, 'Запись обновлена')
        return super().form_valid(form)


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'crud/item_confirm_delete.html'
    success_url = reverse_lazy('crud:list')

    def form_valid(self, form):
        messages.success(self.request, 'Запись удалена')
        return super().form_valid(form)
