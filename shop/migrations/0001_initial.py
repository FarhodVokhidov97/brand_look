# Generated by Django 4.0.4 on 2022-05-21 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Brand name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Category name')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Product name')),
                ('main_image', models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Main product image')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Product description')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Price before sale')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Product price')),
                ('stock', models.PositiveIntegerField(verbose_name='Product stock')),
                ('available', models.BooleanField(default=True, verbose_name='Product available')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.brand', verbose_name='Product brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.category', verbose_name='Product category')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'ordering': ['-price', 'updated', 'created', 'id'],
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Product image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_image', to='shop.product')),
            ],
            options={
                'verbose_name': 'additional image of the product',
                'verbose_name_plural': 'additional images of the product',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Characteristic name')),
                ('value', models.CharField(max_length=200, verbose_name='Characteristic value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='characteristic_items', to='shop.product')),
            ],
            options={
                'verbose_name': 'characteristic',
                'verbose_name_plural': 'Characteristic',
            },
        ),
    ]
