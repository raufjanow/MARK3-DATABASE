from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_product, name='create_product'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('update/<int:pk>/', views.update_product, name='update_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]


