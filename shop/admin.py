from django.contrib import admin

from shop.models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemListAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'currency')
    search_fields = ('name', 'description')


@admin.register(Order)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_items', 'items_cost', 'discount', 'discount_cost', 'tax', 'tax_cost')

    @admin.display(description='Корзина')
    def display_items(self, obj):
        return "\n".join([str(item) for item in obj.items.all()]) or None

    # @admin.display(description='Скидка, %')
    # def discount(self, obj):
    #     discount = Discount.objects.first()
    #     return discount if discount is not None else 0.0
    #
    # @admin.display(description='Стоимость товаров со скидкой')
    # def discount_cost(self, obj):
    #     discount = Discount.objects.first()
    #     if discount is not None:
    #         total_discount = 1 - float(discount.discount) / 100
    #         total_cost = round((float(obj.items_cost) * total_discount), 2)
    #         return total_cost
    #     else:
    #         return float(obj.items_cost)

    # @admin.display(description='Налог, %')
    # def tax(self, obj):
    #     tax = Tax.objects.first()
    #     return tax if tax is not None else 0.0
    #
    # @admin.display(description='Стоимость товаров со скидкой и с налогом')
    # def tax_cost(self, obj):
    #     discount_cost = self.discount_cost(obj)
    #     tax = Tax.objects.first()
    #     if tax is not None:
    #         total_tax = 1 - float(tax.tax) / 100
    #         total_cost = round((discount_cost * total_tax), 2)
    #         return total_cost
    #     else:
    #         return discount_cost


@admin.register(Discount)
class DiscountListAdmin(admin.ModelAdmin):
    ...


@admin.register(Tax)
class TaxListAdmin(admin.ModelAdmin):
    ...
