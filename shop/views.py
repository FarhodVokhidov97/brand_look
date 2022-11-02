from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from .utils import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q


class Home(DataMixin, ListView):
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Why Hub')
        return dict(list(context.items()) + list((c_def.items())))

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Product.objects.filter(Q(name__iregex=query), available=True).select_related('category')
        else:
            return Product.objects.filter(available=True).select_related('category')


class ProductListByCategory(DataMixin, ListView):
    template_name = 'shop/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], available=True).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_image'] = ProductImages.objects.all()
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(
            title='Категорія - ' + str(category.name),
            cat_selected=category.id)
        return dict(list(context.items()) + list((c_def.items())))


class ProductDetail(DataMixin, DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'shop/detail.html'
    context_object_name = 'product'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['characteristics'] = Characteristic.objects.all().filter(product_id=context['product'].id)
        context['product_image'] = ProductImages.objects.all().filter(product_id=context['product'].id)
        context['similar_products'] = Product.objects.filter(id__lt=context['product'].id)[:5]

        if len(context['similar_products']) < 5:
            context['similar_products'] = Product.objects.filter(id__gt=context['product'].id).order_by('pk')[:5]

        c_def = self.get_user_context(title=context['product'].name)
        return dict(list(context.items()) + list((c_def.items())))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('product_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_success_url(self):
        return reverse_lazy('product_list')


def logout_user(request):
    logout(request)
    return redirect('login')
