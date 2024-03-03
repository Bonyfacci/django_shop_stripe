from django.db import models
from django.utils.translation import gettext_lazy as _

from shop.utils import calculate_price

NULLABLE = {'null': True, 'blank': True}


class Item(models.Model):

    CURRENCY = (
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    )

    name = models.CharField(_('Name'), max_length=150)
    description = models.TextField(_('Description'), **NULLABLE)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, default=0.0)

    currency = models.CharField(_('Currency'), max_length=3, choices=CURRENCY, default='RUB')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')
        ordering = ('name',)


class Discount(models.Model):
    discount = models.DecimalField(_('Discount'), max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.discount}'

    class Meta:
        verbose_name = _('Скидка')
        verbose_name_plural = _('Скидки')
        ordering = ('-discount',)


class Tax(models.Model):
    tax = models.DecimalField(_('Tax'), max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.tax}'

    class Meta:
        verbose_name = _('Налог')
        verbose_name_plural = _('Налоги')
        ordering = ('-tax',)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='items_order')

    @property
    def items_cost(self):
        return calculate_price(self.items.all()) or None
    items_cost.fget.short_description = u'Стоимость товаров, руб.'

    @property
    def discount(self):
        discount = Discount.objects.first()
        return discount if discount is not None else 0.0

    discount.fget.short_description = u'Скидка, %'

    @property
    def discount_cost(self):
        discount = Discount.objects.first()
        if discount is not None:
            total_discount = 1 - float(discount.discount) / 100
            total_cost = round((float(self.items_cost) * total_discount), 2)
            return total_cost
        else:
            return float(self.items_cost)

    discount_cost.fget.short_description = u'Стоимость товаров со скидкой, руб'

    @property
    def tax(self):
        tax = Tax.objects.first()
        return tax if tax is not None else 0.0

    tax.fget.short_description = u'Налог, %'

    @property
    def tax_cost(self):
        discount_cost = self.discount_cost
        tax = Tax.objects.first()
        if tax is not None:
            total_tax = 1 + float(tax.tax) / 100
            total_cost = round((discount_cost * total_tax), 2)
            return total_cost
        else:
            return discount_cost

    tax_cost.fget.short_description = u'Стоимость товаров со скидкой и налогом, руб'

    def __str__(self):
        return f''

    class Meta:
        verbose_name = _('Заказ')
        verbose_name_plural = _('Заказы')
        ordering = ('-id',)
