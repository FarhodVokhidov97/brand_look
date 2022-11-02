from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Category name')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_list_by_category',
                       args=[self.slug])


class Brand(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Brand name')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')

    class Meta:
        ordering = ('name',)
        verbose_name = 'brand'
        verbose_name_plural = 'brands'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT,
                                 verbose_name='Product category')
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.PROTECT, verbose_name='Product brand')
    name = models.CharField(max_length=200, db_index=True, verbose_name='Product name')
    main_image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name='Main product image')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, verbose_name='Product description')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True,
                                    verbose_name='Price before sale')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Product price')
    stock = models.PositiveIntegerField(verbose_name='Product stock')
    available = models.BooleanField(default=True, verbose_name='Product available')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-price', 'updated', 'created', 'id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.slug])


class Characteristic(models.Model):
    product = models.ForeignKey('Product', related_name='characteristic_items', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Characteristic name')
    value = models.CharField(max_length=200, verbose_name='Characteristic value')

    class Meta:
        verbose_name = 'characteristic'
        verbose_name_plural = 'Characteristic'

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey('Product', related_name='product_image', on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Product image')

    class Meta:
        verbose_name = 'additional image of the product'
        verbose_name_plural = 'additional images of the product'

    def __str__(self):
        return f'Product image'
