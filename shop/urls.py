from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='product_list'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('<slug:category_slug>/', views.ProductListByCategory.as_view(), name='product_list_by_category'),
    path('product/<slug:product_slug>/', views.ProductDetail.as_view(), name='product_detail'),
]
