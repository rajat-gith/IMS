from django.urls import path
from src.views import store_views as views

urlpatterns=[
    path('',views.getStores,name="stores"),
]

