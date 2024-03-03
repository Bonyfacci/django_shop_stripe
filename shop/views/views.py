import stripe
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View, generic

from config.settings import STRIPE_SECRET_KEY
from shop.models import Item, Order
from shop.services import create_a_payment, create_a_payment_intent


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


class OrderCreateView(generic.CreateView):
    model = Order
    fields = '__all__'

    def get_success_url(self):
        return reverse('shop:order_list')


class OrderListView(generic.ListView):
    model = Order


class OrderUpdateView(generic.UpdateView):
    model = Order
    fields = '__all__'

    def get_success_url(self):
        return reverse('shop:order_list')


class OrderDetailView(generic.DetailView):
    model = Order

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(pk=self.kwargs.get('pk'))
        return queryset


class ItemStripeView(View):

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        try:
            item = Item.objects.get(id=kwargs.get('pk'))
            url_path = request.build_absolute_uri('/')
            url_pay = create_a_payment(item, url_path)
            return redirect(url_pay)
        except Item.DoesNotExist:
            pass


class OrderStripeView(View):

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> JsonResponse:
        try:
            order = Order.objects.get(id=kwargs.get('pk'))

            return JsonResponse(create_a_payment_intent(order))
        except Exception as e:
            return JsonResponse({'error': str(e)})

