from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class Item(models.Model):
    name = models.CharField(_('Name'), max_length=150)
    description = models.TextField(_('Description'), **NULLABLE)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('name',)
