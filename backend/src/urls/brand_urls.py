from django.urls import path
from src.views import brand_views as views

urlpatterns=[
    path('',views.getBrands,name="store"),
    
]

