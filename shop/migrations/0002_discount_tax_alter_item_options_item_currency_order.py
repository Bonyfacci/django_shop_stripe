# Generated by Django 5.0.2 on 2024-03-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Discount')),
            ],
            options={
                'verbose_name': 'Скидка',
                'verbose_name_plural': 'Скидки',
                'ordering': ('-discount',),
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tax', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Tax')),
            ],
            options={
                'verbose_name': 'Налог',
                'verbose_name_plural': 'Налоги',
                'ordering': ('-tax',),
            },
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(choices=[('RUB', 'RUB'), ('USD', 'USD'), ('EUR', 'EUR')], default=1, max_length=3, verbose_name='Currency'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Total cost')),
                ('items', models.ManyToManyField(related_name='items_order', to='shop.item')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('total_cost',),
            },
        ),
    ]
