from django.contrib import admin
from django.urls import path,include
from backend import views

urlpatterns = [
    path("", views.homepage),
    path("admin/", admin.site.urls),
    path("api/users/",include('src.urls.user_urls')),
    path("api/stores/",include('src.urls.store_urls')),
    path("api/products/",include('src.urls.product_urls'))
]
