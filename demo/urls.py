from django.urls import path

from . import views

urlpatterns = [
    path('', views.demo_page, name='confirm_account'),
]