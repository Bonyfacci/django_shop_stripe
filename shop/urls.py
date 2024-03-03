from django.urls import path

from shop.apps import ShopConfig
from shop.views.views import home, ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemDetailView, \
    OrderListView, OrderCreateView, OrderDetailView, OrderUpdateView, ItemStripeView, OrderStripeView
from shop.views.views_api import ItemListAPIView, ItemCreateAPIView, ItemUpdateAPIView, ItemDeleteAPIView, \
    ItemDetailAPIView

app_name = ShopConfig.name

urlpatterns = [
    path('', home, name='home'),

    # Item (frontend)
    path('items/', ItemListView.as_view(), name='item_list'),
    path('item/create/', ItemCreateView.as_view(), name='item_create'),
    path('item/edit/<int:pk>/', ItemUpdateView.as_view(), name='item_edit'),
    path('item/delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_article'),

    # Item (api view)
    path('api/items/', ItemListAPIView.as_view(), name='item-list'),
    path('api/item/create/', ItemCreateAPIView.as_view(), name='item-create'),
    path('api/item/edit/<int:pk>/', ItemUpdateAPIView.as_view(), name='item-edit'),
    path('api/item/delete/<int:pk>/', ItemDeleteAPIView.as_view(), name='item-delete'),
    path('api/item/<int:pk>/', ItemDetailAPIView.as_view(), name='item-article'),

    # Order
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/edit/<int:pk>/', OrderUpdateView.as_view(), name='order_edit'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_article'),

    # Stripe
    path('buy/<int:pk>/', ItemStripeView.as_view(), name='buy_item_stripe'),
    path('buy/order/<int:pk>/', OrderStripeView.as_view(), name='buy_order_stripe'),


]
