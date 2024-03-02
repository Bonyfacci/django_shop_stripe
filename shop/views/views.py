from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View, generic
from shop.models import Item
from shop.services import create_a_payment


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name='shop/home.html',
        context={},
    )


class ItemListView(generic.ListView):
    model = Item


class ItemCreateView(generic.CreateView):
    model = Item
    fields = '__all__'

    def get_success_url(self):
        return reverse('shop:item_list')


class ItemUpdateView(generic.UpdateView):
    model = Item
    fields = '__all__'

    def get_success_url(self):
        return reverse('shop:item_list')


class ItemDeleteView(generic.DeleteView):
    model = Item


class ItemDetailView(generic.DetailView):
    model = Item

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset


class StripeView(View):

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        item = Item.objects.get(id=kwargs.get('pk'))
        url_path = request.build_absolute_uri('/')
        url_pay = create_a_payment(item, url_path)
        return redirect(url_pay)
