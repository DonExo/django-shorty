from django.contrib import admin
from django.urls import path
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<str:shorty>', views.redirecto),
]
