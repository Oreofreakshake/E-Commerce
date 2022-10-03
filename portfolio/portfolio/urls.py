from pages.views import Home_view, Main_view
from product.views import product_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", Main_view),
    path("home/", Home_view),
    path("products/", product_view),
    path("admin/", admin.site.urls),
]
