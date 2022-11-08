from django.urls import path
from src.views import store_views as views

urlpatterns=[
    path('',views.getStoreOwners,name="store_owners"),
    path('<int:pk>/',views.getStoreOwnerById,name="store_owner"),

]

