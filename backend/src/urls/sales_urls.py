from django.urls import path
from src.views import store_views as views

urlpatterns=[
    path('',views.getSales,name="sales"),
    path('add/',views.creatSales,name="addsales"),
    path('<str:pk>/',views.getSalesById,name="sale"),

    
]
