from django.urls import path
from src.views import product_views as views


urlpatterns=[
    path('brands/',views.getBrands,name="brands"),
    path('brands/<str:pk>/',views.getBrandsById,name="brand"),
    path('',views.getProducts,name="products"),
    path('<int:pk>/',views.getProductsById,name="product"),
    path('add/',views.addProduct,name="addProduct")
]